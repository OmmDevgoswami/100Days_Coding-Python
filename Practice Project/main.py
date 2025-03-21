from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import os
import dotenv

dotenv.load_dotenv()
FLA_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = FLA_SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)
bootstrap = Bootstrap5(app)
all_books = []

class BookForm(FlaskForm):
    title = StringField('Book Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    Rating = SelectField('Rating', validators=[DataRequired()],choices=[(str(i)) for i in range(1,11)])
    submit = SubmitField('Add Book')

@app.route('/')
def home():
    return render_template("index.html", books = all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        book_details = {"title" : form.title.data, "author" : form.author.data, "rating" : form.Rating.data}
        all_books.append(book_details)
        return redirect(url_for('home'))
    
    return render_template("add.html", form = form)

if __name__ == "__main__":
    app.run(debug=True)

