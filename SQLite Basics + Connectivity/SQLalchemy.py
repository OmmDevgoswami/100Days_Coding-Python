from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
    __tablename__ = "book"
    id : Mapped[int] = mapped_column(Integer, primary_key = True)
    title : Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    author : Mapped[str] = mapped_column(String(50), nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=False)
    
####### Creating : C
# with app.app_context():
#     db.create_all()

# with app.app_context():
#     new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()
    
####### Reading : R
#### Multivalue
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars().all() 

#     for book in all_books:
#         print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Rating: {book.rating}")
        
#### Singlevalue  
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

#     if book:
#         print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Rating: {book.rating}")
#     else:
#         print("Book not found")

######## Updating : U
#### Using selector
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit() 
    
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter and the Chamber of Secrets")).scalar()

#     if book:
#         print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Rating: {book.rating}")
#     else:
#         print("Book not found")

##### Using Primary Key
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)  
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit() 
    
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter and the Goblet of Fire")).scalar()

#     if book:
#         print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Rating: {book.rating}")
#     else:
#         print("Book not found")
        
############ Deleteing : D
book_id = 1
with app.app_context():
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    print("Deleted")