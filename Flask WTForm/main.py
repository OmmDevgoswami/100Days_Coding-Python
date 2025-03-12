from flask import Flask, render_template, request, make_response
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
        # resp = make_response(f"""Form submitted successfully! <br />
        # Name: {form.name.data} <br />
        # Email: {form.email.data} <br />
        # Password: {form.password.data}""")
        return render_template('success.html')
    if form.validate_on_submit():
        return render_template('denied.html')
    
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
