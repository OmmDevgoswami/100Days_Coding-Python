from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

name = "Omm"
randomNumber = random.random()
year = dt.datetime.now()
currentYear = year.year

@app.route("/")
def home():
    return render_template("index.html", num=randomNumber, year = currentYear, name = name)

@app.route("/guess/<number>")
def guess_page(number):
    def genderFinder():
            gender = requests.get("https://api.genderize.io", params = {"name": name})
            gender.raise_for_status()
            genderGuess = gender.json()
            return genderGuess["gender"]
    def ageFinder():
            age = requests.get("https://api.agify.io", params = {"name": name})
            age.raise_for_status()
            ageGuess = age.json()
            return ageGuess["age"]
        
    gender = genderFinder()
    age = ageFinder()
    return render_template("guess.html", user_name = name, gender = gender, age = age, num = number)

@app.route("/blog")
def blog_page():
    response = requests.get(" https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    allPosts = response.json()
    return render_template("fake_blog.html", posts = allPosts)
    
if __name__ == "__main__":
    app.run(debug = True)