from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os
import dotenv
from datetime import datetime

dotenv.load_dotenv()
FLA_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = FLA_SECRET_KEY
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)



# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    
class Blog_New_Post(FlaskForm):
    title = StringField("Blog Post Title", validators = [DataRequired()])
    subtitle = StringField("Subtitle", validators = [DataRequired()])
    date = DateField("Date", validators = [DataRequired()], format="%Y-%m-%d")
    author = StringField("Author", validators = [DataRequired()])
    body = CKEditorField("Blog Post", validators = [DataRequired()])
    img_url = URLField("Image URL", validators = [DataRequired(), URL()])
    submit = SubmitField("Add Blog Post")

# with app.app_context():
#     db.create_all()
    
# with app.app_context():
#     new_blog_1 = BlogPost(
#         title="Blog Post 1",
#         subtitle="Subtitle 1",
#         date=date.today().strftime("%B %d, %Y"),
#         body="Body 1",
#         author="Author 1",
#         img_url="https://www.example.com/image1.jpg"
#     )
#     db.session.add(new_blog_1)
#     db.session.commit()
    
#     new_blog_2 = BlogPost(
#         title="Blog Post 2",
#         subtitle="Subtitle 2",
#         date=date.today().strftime("%B %d, %Y"),
#         body="Body 2",
#         author="Author 2",
#         img_url="https://www.example.com/image1.jpg"
#     )
#     db.session.add(new_blog_2)
#     db.session.commit()
    
#     new_blog_3 = BlogPost(
#         title="Blog Post 3",
#         subtitle="Subtitle 3",
#         date=date.today().strftime("%B %d, %Y"),
#         body="Body 3",
#         author="Author 3",
#         img_url="https://www.example.com/image1.jpg"
#     )
#     db.session.add(new_blog_3)
#     db.session.commit()


@app.route('/')
def get_all_posts():
    blogs = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=blogs)

@app.route('/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)

@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    form = Blog_New_Post()
    if form.validate_on_submit():
        new_blog = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=form.date.data.strftime("%B %d, %Y"),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data   
            )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form = form, mode = "new")

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    edit_form = Blog_New_Post(
            title = requested_post.title,
            subtitle = requested_post.subtitle,
            img_url = requested_post.img_url,
            author = requested_post.author,
            date = datetime.strptime(requested_post.date, "%B %d, %Y").date(), 
            body = requested_post.body
    )
    if edit_form.validate_on_submit():
        requested_post.title = edit_form.title.data
        requested_post.subtitle = edit_form.subtitle.data
        requested_post.author = edit_form.author.data
        requested_post.date = edit_form.date.data.strftime("%B %d, %Y")
        requested_post.body = edit_form.body.data
        requested_post.img_url = edit_form.img_url.data
        db.session.commit()
        return redirect(url_for('show_post', post_id = post_id))
    return render_template("make-post.html", form = edit_form, mode = "edit")
    
# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>", methods=["GET", "POST"])
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
