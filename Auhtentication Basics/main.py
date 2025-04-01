from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
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
            flash("User not found!", "error")
            return redirect(url_for("login"))
        
        if not check_password_hash(existing_user.password, request.form.get("password")):
            flash("Password is Wrong!", "error")
            return redirect(url_for("login"))
        
        flash("Login Successfull")
        return redirect(url_for('secrets', userID = existing_user.id))
    
    return render_template("login.html")


@app.route('/secrets/<int:userID>')
def secrets(userID):
    user = db.get_or_404(User, userID)
    
    if not user:
        flash("User not found!", "error")
        return redirect(url_for("register"))

    return render_template("secrets.html", user_name = user.name)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('static/files', "cheat_sheet.pdf", as_attachment = True)
    # "as_attachment=True" in case we want to make the file download


if __name__ == "__main__":
    app.run(debug=True)
