from flask import Flask

def makeBold(elements):
    def wrapper():
        element = elements()
        return f"<b>{element}</b>"
    return wrapper

def makeUnderline(elements):
    def wrapper():
        element = elements()
        return f"<u>{element}</u>"
    return wrapper

def makeItalic(elements):
    def wrapper():
        element = elements()
        return f"<i>{element}</i>"
    return wrapper


app = Flask(__name__)

@app.route("/")         #/ incideates to the Home page
def hello_world():
    return "<p> Hello World </p>"

@app.route("/bye")      #/bye is another page
@makeBold
@makeItalic
@makeUnderline
def bye_world():
    return "<p> Bye World </p>"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"<h1>Hello, {name}! You are {number} years old.</h1>"

if __name__ == "__main__":
    app.run(debug = True)