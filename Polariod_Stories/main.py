from flask import Flask, render_template, url_for, request, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort
from flask_login import current_user
from forms import RegisterForm, LoginForm
import time

import os
import dotenv
dotenv.load_dotenv()

app = Flask(__name__)
Bootstrap5(app)
FLASK_SECRETS = os.getenv("FLASK_SECRETS")
app.config['SECRET_KEY'] = FLASK_SECRETS

login_manager = LoginManager()
login_manager.init_app(app)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///polaroid_users.db')
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    role: Mapped[str] = mapped_column(String(50), default="user")
    
with app.app_context():
    db.create_all()

current_year = time.localtime().tm_year

@app.route("/")
def home():
    return render_template("index.html", year=current_year)

@app.route("/contact")
def contacts():
    return render_template("contact.html", year=current_year)

@app.route("/canvas")
def canvas():
    return render_template("canvas.html", year=current_year)

@app.route('/register', methods = ["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if request.method == "POST":
            email = request.form.get("email")
            existing_user = User.query.filter_by(email=email).first()
            
            if existing_user:
                flash("User already exists! Please log in.")
                return redirect(url_for('login'))
            
            new_user = User(
                email=request.form.get("email"),
                password=generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8),
                name=request.form.get("name"),
                role="user"
            )
            
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash("Registration Successful")
            return redirect(url_for('home'))
    return render_template("register.html", form=form, year=current_year)

@app.route('/login', methods = ["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            user = User.query.filter_by(email=email).first()
            
            if not user:
                flash("Wrong Credentials Entered!! Please try again.")
                return redirect(url_for('login'))
            
            if not check_password_hash(user.password, password):
                flash("Wrong Credentials Entered!! Please try again.")
                return redirect(url_for('login'))
            
            login_user(user)
            return redirect(url_for('home'))
        flash("Login Successful")
        return redirect(url_for('home'))
    return render_template("login.html", form=form, year=current_year)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)