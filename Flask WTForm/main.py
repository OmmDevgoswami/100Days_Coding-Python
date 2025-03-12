from flask import Flask, render_template
import os
import dotenv
from forms import MyForm

dotenv.load_dotenv()
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        return "Form submitted successfully!"
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
