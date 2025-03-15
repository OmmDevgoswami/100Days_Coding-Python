from flask import Flask, render_template, request, make_response
import os
import dotenv
from forms import MyForm
from flask_bootstrap import Bootstrap5

dotenv.load_dotenv()
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ["POST", "GET"])
def login():
    form = MyForm()
        
    if form.validate_on_submit():
        # resp = make_response(f"""Form submitted successfully! <br />
        # Name: {form.name.data} <br />
        # Email: {form.email.data} <br />
        # Password: {form.password.data}""")
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
