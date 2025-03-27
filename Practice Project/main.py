from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
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
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
db.init_app(app)
bootstrap = Bootstrap5(app)
# all_books = []

class Book(db.Model):
    __tablename__ = "Book Details"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    bookTitle : Mapped[str] = mapped_column(String(50), unique = True, nullable = False)
    bookAuthor : Mapped[str] = mapped_column(String(50), nullable = False)
    bookRating : Mapped[float] = mapped_column(Float, nullable = False)

# with app.app_context():
#     db.create_all()

class BookForm(FlaskForm):
    title = StringField('Book Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    Rating = SelectField('Rating', validators=[DataRequired()],choices=[(str(i)) for i in range(1,11)])
    submit = SubmitField('Add Book')

@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.id))
        all_books = result.scalars().all()
        
    return render_template("index.html", books = all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        # book_details = {"title" : form.title.data, "author" : form.author.data, "rating" : form.Rating.data}
        # all_books.append(book_details)
        with app.app_context():
            new_book = Book(bookTitle = form.title.data, bookAuthor = form.author.data, bookRating = form.Rating.data)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("add.html", form = form)

class RatingForm(FlaskForm):
    rating = SelectField('Rating', choices=[(str(i), str(i)) for i in range(1, 11)], validators=[DataRequired()])
    submit = SubmitField('Update Rating')

@app.route("/rating", methods=['GET', 'POST'])
def rating():
    book_id_val = request.args.get("book_id", type=int) 
    book = db.get_or_404(Book, book_id_val)  

    form = RatingForm()
    if form.validate_on_submit():
        book.bookRating = float(form.rating.data)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("changeRating.html", form=form, value=book.bookRating)

@app.route("/delete", methods=['GET', 'POST'])
def deleting():
    book_id_val = request.args.get("book_id", type=int) 
    book = db.get_or_404(Book, book_id_val)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

