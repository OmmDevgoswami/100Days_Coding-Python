from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
import requests
import os
import dotenv

dotenv.load_dotenv()
FLA_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = FLA_SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///10_movies.db"
db.init_app(app)
Bootstrap5(app)

# CREATE DB
class Movies(db.Model):
  __tablename__ = "Movie Details"
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  title : Mapped[str] = mapped_column(String(20), unique = True, nullable = False)
  year : Mapped[int] = mapped_column(Integer, nullable = False)
  rating : Mapped[float] = mapped_column(Float, nullable = False)
  ranking : Mapped[int] = mapped_column(Integer, nullable = False)
  review : Mapped[str] = mapped_column(String(100), nullable = False)
  overview : Mapped[str] = mapped_column(String(200), nullable = False)
  img_url : Mapped[str] = mapped_column(String(100), nullable = False)
  
class Movie_Archieve(FlaskForm):
  title = StringField("Movie Title", validators = [DataRequired()])
  year = IntegerField("Release Year", validators = [DataRequired()])
  rating = SelectField("Rating ⭐", validators = [DataRequired()], default = "0.0", choices = [(f"{i/10:.1f}", f"{i/10:.1f}") for i in range(10, 101, 5)])
  ranking = IntegerField("Ranking", validators = [DataRequired()])
  review = StringField("Perosnal Review", validators = [DataRequired()])
  overview = StringField("Movie Overview", validators = [DataRequired()])
  img_url = StringField("Movie Poster URL", validators = [DataRequired()])
  submit = SubmitField("Add Movie")

# CREATE TABLE
# with app.app_context():
#   db.create_all()
  
# with app.app_context():
#   new_movie = Movies(
#     title = "Bubble",
#     year = 2022,
#     rating = 8.9,
#     ranking = 10,
#     review = "This movie is so good!",
#     overview = "This is one of the most amazing and touching anime from the Studio with the unique blend of Parkhor, Song and Light-enhancing Bubbles",
#     img_url = "https://m.media-amazon.com/images/M/MV5BNjMzNmFjZWItMjZlZS00OTgwLTgwMmMtYTc5MTA0MTY2MGEwXkEyXkFqcGc@._V1_.jpg"
#   )
#   db.session.add(new_movie)
#   db.session.commit()


@app.route("/")
def home():
    with app.app_context():
        movies = db.session.execute(db.select(Movies).order_by(Movies.ranking.desc()))
        all_movies = movies.scalars().all()
    return render_template("index.html", movies=all_movies) 

  
@app.route("/add",  methods=["GET", "POST"])
def add():
    form = Movie_Archieve()
    if form.validate_on_submit():
      with app.app_context():
        new_movie = Movies(title = form.title.data,
              year = form.year.data,
              rating = float(form.rating.data),
              ranking = form.ranking.data,
              review = form.review.data,
              overview = form.overview.data,
              img_url = form.img_url.data
            )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form = form)
  
@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id_val = request.args.get("movie_id", type=int)
    movie = db.get_or_404(Movies, movie_id_val)

    form = Movie_Archieve(obj=movie)  

    if form.validate_on_submit():
        movie.rating = float(form.rating.data) 
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=form, value=movie)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    movie_id_val = request.args.get("movie_id", type=int)
    movie = db.get_or_404(Movies, movie_id_val)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))
    

if __name__ == '__main__':
    app.run(debug=True)
