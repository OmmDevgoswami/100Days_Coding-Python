from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    data = response.json()
    
    return render_template("index.html", posts = data)

@app.route("/post/<postNo>")
def post_page(postNo):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    data = response.json()
    
    post_data = None
    for _ in data:
        if _["id"] == int(postNo):
            post_data = _
            break
    return render_template("post.html", post = post_data)

if __name__ == "__main__":
    app.run(debug=True)
