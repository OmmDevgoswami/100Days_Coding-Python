from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, Length
from datetime import datetime
import os
import dotenv
dotenv.load_dotenv()

FLASK_SECRETS = os.getenv("FLASK_SECRETS")
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = FLASK_SECRETS
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'bank.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# MODELS
class Customer(db.Model):
    cust_no = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phoneno = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    accounts = db.relationship('Account', backref='customer', lazy=True)
    loans = db.relationship('Loan', backref='customer', lazy=True)

class Account(db.Model):
    account_no = db.Column(db.String, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Float, default=0)
    cust_no = db.Column(db.String, db.ForeignKey('customer.cust_no'))
    branch_code = db.Column(db.String)
    branch_name = db.Column(db.String)
    branch_city = db.Column(db.String)

class Loan(db.Model):
    loan_no = db.Column(db.String, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    cust_no = db.Column(db.String, db.ForeignKey('customer.cust_no'))
    branch_code = db.Column(db.String)
    branch_name = db.Column(db.String)
    branch_city = db.Column(db.String)
    
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_no = db.Column(db.String, db.ForeignKey('account.account_no'), nullable=False)
    type = db.Column(db.String(10))  # 'deposit' or 'withdraw'
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(200))

    account = db.relationship('Account', backref='transactions')

# FORMS
class CustomerForm(FlaskForm):
    cust_no = StringField('Customer No', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    phoneno = StringField('Phone No', validators=[DataRequired(), Length(min=10, max=15)])
    city = StringField('City', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateCustomerForm(FlaskForm):
    name = StringField('Name')
    phoneno = StringField('Phone No')
    city = StringField('City')
    submit = SubmitField('Update')

class MoneyForm(FlaskForm):
    account_no = StringField('Account No', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

# ROUTES
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/customers')
def customers():
    all_customers = Customer.query.all()
    return render_template('customers.html', customers=all_customers)

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        existing = Customer.query.get(form.cust_no.data)
        if existing:
            flash('Customer with this ID already exists.', 'danger')
            return redirect(url_for('customers'))
        cust = Customer(
            cust_no=form.cust_no.data,
            name=form.name.data,
            phoneno=form.phoneno.data,
            city=form.city.data
        )
        db.session.add(cust)
        db.session.commit()
        flash('Customer added successfully!', 'success')
        return redirect(url_for('customers'))
    return render_template('add_customer.html', form=form)

@app.route('/delete_customer/<cust_no>')
def delete_customer(cust_no):
    customer = Customer.query.get(cust_no)
    if customer:
        db.session.delete(customer)
        db.session.commit()
        flash('Customer deleted successfully.', 'success')
    else:
        flash('Customer not found.', 'danger')
    return redirect(url_for('customers'))

@app.route('/update_customer/<cust_no>', methods=['GET', 'POST'])
def update_customer(cust_no):
    customer = Customer.query.get(cust_no)
    if not customer:
        flash('Customer not found.', 'danger')
        return redirect(url_for('customers'))
    form = UpdateCustomerForm(obj=customer)
    if form.validate_on_submit():
        if form.name.data:
            customer.name = form.name.data
        if form.phoneno.data:
            customer.phoneno = form.phoneno.data
        if form.city.data:
            customer.city = form.city.data
        db.session.commit()
        flash('Customer updated successfully.', 'success')
        return redirect(url_for('customers'))
    return render_template('update_customer.html', form=form, customer=customer)

@app.route('/account_details/<cust_no>')
def account_details(cust_no):
    customer = Customer.query.get(cust_no)
    return render_template('account_details.html', customer=customer)

@app.route('/loan_details/<cust_no>')
def loan_details(cust_no):
    customer = Customer.query.get(cust_no)
    if not customer:
        flash("Customer not found.", "danger")
        return redirect(url_for("customers"))

    loan_list = [
        {
            'Loan No': loan.loan_no,
            'Amount': loan.amount,
            'Branch Code': loan.branch_code,
            'Branch Name': loan.branch_name,
            'Branch City': loan.branch_city
        }
        for loan in customer.loans
    ]
    return render_template('loan_details.html', customer=customer, details=loan_list, type="loan", title="Loan Details")


@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    form = MoneyForm()
    if form.validate_on_submit():
        acc = Account.query.get(form.account_no.data)
        if not acc:
            flash('Account not found.', 'danger')
        else:
            acc.balance += form.amount.data
            db.session.commit()
            flash(f'Deposited ₹{form.amount.data} successfully.', 'success')
            txn = Transaction(account_no=acc.account_no, type='deposit',
                  amount=form.amount.data, description='Deposit to account')
            db.session.add(txn)
        return redirect(url_for('home'))
    return render_template('deposit.html', form=form)

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    form = MoneyForm()
    if form.validate_on_submit():
        acc = Account.query.get(form.account_no.data)
        if not acc:
            flash('Account not found.', 'danger')
        elif acc.balance < form.amount.data:
            flash('Insufficient balance.', 'danger')
        else:
            acc.balance -= form.amount.data
            db.session.commit()
            flash(f'Withdrew ₹{form.amount.data} successfully.', 'success')
            txn = Transaction(account_no=acc.account_no, type='withdraw',
                  amount=form.amount.data, description='Withdraw from account')
            db.session.add(txn)
        return redirect(url_for('home'))
    return render_template('withdraw.html', form=form)

@app.route('/transactions/<account_no>')
def transactions(account_no):
    acc = Account.query.get(account_no)
    if not acc:
        flash('Account not found.', 'danger')
        return redirect(url_for('home'))
    return render_template('transactions.html', account=acc, transactions=acc.transactions)

if __name__ == '__main__':
    with app.app_context():
        # db.create_all()

        # # Insert customers
        # if not Customer.query.first():
        #     customers = [
        #         Customer(cust_no='C0001', name='RAJ ANAND SINGH', phoneno='9861258466', city='DELHI'),
        #         Customer(cust_no='C0002', name='ANKITA SINGH', phoneno='9879958651', city='BANGALORE'),
        #         Customer(cust_no='C0003', name='SOUMYA JHA', phoneno='9885623344', city='MUMBAI'),
        #         Customer(cust_no='C0004', name='ABHIJIT MISHRA', phoneno='9455845425', city='MUMBAI'),
        #         Customer(cust_no='C0005', name='YASH SARAF', phoneno='9665854585', city='KOLKATA'),
        #         Customer(cust_no='C0006', name='SWAROOP RAY', phoneno='9437855466', city='CHENNAI'),
        #         Customer(cust_no='C0007', name='SURYA NARAYAN PRADHAN', phoneno='9937955212', city='GURGAON'),
        #         Customer(cust_no='C0008', name='PRANAV PRAVEEN', phoneno='9336652441', city='PUNE'),
        #         Customer(cust_no='C0009', name='STUTI MISRA', phoneno='7870266534', city='DELHI'),
        #         Customer(cust_no='C0010', name='ASLESHA TIWARI', phoneno='0000000000', city='MUMBAI'),
        #     ]
        #     db.session.bulk_save_objects(customers)
        #     db.session.commit()
        #     print("✅ Customers inserted.")
        
        # # Insert accounts with zero balance
        # if not Account.query.first():
        #     accounts = [
        #         Account(account_no='A0001', type='SB', balance=0, cust_no='C0003', branch_code='B003', branch_name='JUHU BRANCH', branch_city='MUMBAI'),
        #         Account(account_no='A0002', type='SB', balance=0, cust_no='C0004', branch_code='B002', branch_name='CHANDNICHOWK BRANCH', branch_city='DELHI'),
        #         Account(account_no='A0003', type='CA', balance=0, cust_no='C0006', branch_code='B004', branch_name='ANDHERI BRANCH', branch_city='MUMBAI'),
        #         Account(account_no='A0004', type='CA', balance=0, cust_no='C0006', branch_code='B004', branch_name='ANDHERI BRANCH', branch_city='MUMBAI'),
        #         Account(account_no='A0005', type='FD', balance=0, cust_no='C0001', branch_code='B005', branch_name='SALTLAKE BRANCH', branch_city='KOLKATA'),
        #         Account(account_no='A0006', type='FD', balance=0, cust_no='C0010', branch_code='B005', branch_name='SALTLAKE BRANCH', branch_city='KOLKATA'),
        #         Account(account_no='A0007', type='SB', balance=0, cust_no='C0009', branch_code='B001', branch_name='JANAKPURI BRANCH', branch_city='DELHI'),
        #         Account(account_no='A0008', type='SB', balance=0, cust_no='C0008', branch_code='B002', branch_name='CHANDNICHOWK BRANCH', branch_city='DELHI'),
        #         Account(account_no='A0009', type='SB', balance=0, cust_no='C0007', branch_code='B003', branch_name='JUHU BRANCH', branch_city='MUMBAI'),
        #         Account(account_no='A0010', type='FD', balance=0, cust_no='C0006', branch_code='B004', branch_name='ANDHERI BRANCH', branch_city='MUMBAI'),
        #     ]
        #     db.session.bulk_save_objects(accounts)
        #     db.session.commit()
        #     print("✅ Accounts inserted.")

        # # Insert loans
        # if not Loan.query.first():
        #     loans = [
        #         Loan(loan_no='L0001', amount=3000000, cust_no='C0005', branch_code='B006', branch_name='SRIRAMPURAM BRANCH', branch_city='CHENNAI'),
        #         Loan(loan_no='L0002', amount=50000, cust_no='C0001', branch_code='B005', branch_name='SALTLAKE BRANCH', branch_city='KOLKATA'),
        #         Loan(loan_no='L0003', amount=8000000, cust_no='C0002', branch_code='B004', branch_name='ANDHERI BRANCH', branch_city='MUMBAI'),
        #         Loan(loan_no='L0004', amount=100000, cust_no='C0010', branch_code='B004', branch_name='ANDHERI BRANCH', branch_city='MUMBAI'),
        #         Loan(loan_no='L0005', amount=9500000, cust_no='C0009', branch_code='B005', branch_name='SALTLAKE BRANCH', branch_city='KOLKATA'),
        #         Loan(loan_no='L0006', amount=25000, cust_no='C0008', branch_code='B006', branch_name='SRIRAMPURAM BRANCH', branch_city='CHENNAI'),
        #     ]
        #     db.session.bulk_save_objects(loans)
        #     db.session.commit()
        #     print("✅ Loans inserted.")
        
        # # Insert sample transactions
        # if not Transaction.query.first():
        #     transactions = [
        #         Transaction(account_no='A0001', type='deposit', amount=50000, description='Initial deposit'),
        #         Transaction(account_no='A0001', type='withdraw', amount=10000, description='ATM withdrawal'),
        #         Transaction(account_no='A0002', type='deposit', amount=15000, description='Salary credited'),
        #         Transaction(account_no='A0003', type='deposit', amount=850000, description='Business income'),
        #         Transaction(account_no='A0004', type='withdraw', amount=5000, description='Utility bill payment'),
        #         Transaction(account_no='A0005', type='deposit', amount=28500, description='Fixed deposit creation'),
        #         Transaction(account_no='A0006', type='deposit', amount=100000, description='Bonus'),
        #         Transaction(account_no='A0007', type='withdraw', amount=12000, description='Online purchase'),
        #         Transaction(account_no='A0008', type='deposit', amount=7200, description='Savings'),
        #         Transaction(account_no='A0010', type='withdraw', amount=9000, description='Loan EMI'),
        #     ]
        #     db.session.bulk_save_objects(transactions)
        #     db.session.commit()
        #     print("✅ Transactions inserted.")
            
        # Update account balances from transactions
        accounts = Account.query.all()
        for acc in accounts:
            balance = 0
            for txn in acc.transactions:
                if txn.type == 'deposit':
                    balance += txn.amount
                elif txn.type == 'withdraw':
                    balance -= txn.amount
            acc.balance = balance
        db.session.commit()
        print("✅ Account balances updated from transactions.")

        app.run(debug=True)

