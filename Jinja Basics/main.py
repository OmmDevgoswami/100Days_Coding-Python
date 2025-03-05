from flask import Flask, render_template
import random
import datetime as dt

app = Flask(__name__)

name = "Omm Devgoswami"
randomNumber = random.random()
year = dt.datetime.now()
currentYear = year.year

@app.route("/")
def home():
    return render_template("index.html", num=randomNumber, year = currentYear, name = name)

if __name__ == "__main__":
    app.run(debug = True)