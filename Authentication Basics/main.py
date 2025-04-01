from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = "login"

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("User already exists! Please log in.")
            return redirect(url_for('login'))
        
        new_user = User(
            email = request.form.get("email"),
            password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8),
            name = request.form.get("name")
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash("Registraion Successfull")
        return redirect(url_for('secrets', userID = new_user.id))
    
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = db.session.execute(db.select(User).where(User.email == request.form.get("email"))).scalar_one_or_none()
        if not existing_user:
            flash("Wrong Credentials Entered !!", "error")
            return redirect(url_for("login"))
        
        if not check_password_hash(existing_user.password, request.form.get("password")):
            flash("Wrong Credentials Entered !!", "error")
            return redirect(url_for("login"))
        
        login_user(existing_user)
        
        flash("Login Successfull")
        return redirect(url_for('secrets', userID = existing_user.id))
    
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", user_name = current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files', "cheat_sheet.pdf", as_attachment = True)

if __name__ == "__main__":
    app.run(debug=True)
