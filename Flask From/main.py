from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods = ["POST"])
def login():
    username = request.form["floatingInput"]
    email = request.form["floatingEmail"]
    password = request.form["floatingPassword"]
    return f"""<h1> Name: {username}, </h1>
<h1>Email: {email} and Password: {password} </h1>"""

if __name__ == "__main__":
    app.run(debug = True)