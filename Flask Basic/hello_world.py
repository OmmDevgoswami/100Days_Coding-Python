from flask import Flask

app = Flask(__name__)

@app.route("/")         #/ incideates to the Home page
def hello_world():
    return "<p> Hello World </p>"

@app.route("/bye")      #/bye is another page
def bye_world():
    return "<p> Bye World </p>"

if __name__ == "__main__":
    app.run()