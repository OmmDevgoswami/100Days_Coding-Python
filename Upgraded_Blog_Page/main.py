from flask import Flask, render_template, request, redirect, url_for
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv("EMAIL_ID")
PASSWORD = os.getenv("PASSKEY")

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    data = response.json()
    
    return render_template("index.html", posts = data)

# @app.route("/about.html")
# def about():
#     return render_template("about.html")

# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")

#A more innovative Solution
@app.route("/<filename>")
def pages(filename):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    data = response.json()
    return render_template(filename, posts = data)

@app.route("/post/<postNo>")
def post_page(postNo):
    response = requests.get("https://api.npoint.io/5808b1a3304a496f4c65")
    response.raise_for_status()
    data = response.json()
    
    post_data = None
    for _ in data:
        if _["id"] == int(postNo):
            post_data = _
            break
    return render_template("post.html", post = post_data)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=email,
                msg=f"Subject: Queries\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            )

        return redirect(url_for("contact"))

    return render_template("contact.html") 

if __name__ == "__main__":
    app.run(debug=True)