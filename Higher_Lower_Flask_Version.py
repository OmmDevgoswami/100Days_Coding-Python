from flask import Flask
import random

def center_everything(functions):
    def wrapper(*args):
        function = functions()
        return f"<div style='text-align:center'> {function} </div>"
    return wrapper
    
app = Flask(__name__)

@app.route("/")
@center_everything
def homePage():
    return """
<h1> Guess a Number from the Range of 1 - 10 </h1>
<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2Y1bW9kMHkyOXJ1OTQ2cHo2M2dpY2liN3FsdXlzZnRid2dkaGRxYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UDU4oUJIHDJgQ/giphy.gif' alt='counter'>
"""

randomNumber = random.randint(1,10)

@center_everything
def lower():
    gifList = ["https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTBvOTV1d3kxN3FveGZtYXNhNmV6YWUyZzl0aDgyemd2dnViMWd6ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IevhwxTcTgNlaaim73/giphy.gif",
               "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExejAyMWNmM2R6NDk1bml1bmY3ajFibWdnYmllYnFhMHR3ZnZ5Z3ptYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT8qB4KH2hCnlMiflu/giphy.gif"]
    image = random.choice(gifList)
    return f"""
<h1> You Guessed Too Lowwwwwwww! Think High </h1>
<img src={image} alt='lower_number'>
"""

@center_everything
def higher():
    gifList = ["https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWZuOHNzNW10ZnJycjhvYnZicXExZ2dzeDZjM2FkMGN5bzJ3c2hubSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xkheXEJSIIvJ3J4YNa/giphy.gif",
               "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExajdvcGNiNWkxN3kzZTQ5djg2ZDZ0Z2s4dHJsa2UzbWxqc2l0dXQ0YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3hJBLbMMjNDmb9jqmO/giphy.gif"]
    image = random.choice(gifList)
    return f"""
<h1> You Guesse is too High !! Get Down a bitttt </h1>
<img src={image} alt='lower_number'>
"""

@center_everything
def correct():
    gifList = ["https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3Bsa2Q1d3pnbDQ5Znh3bGVmazFzam1tNzU2NXBpMXNmNGY2d3pldCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ohMtDzrhrWgnK/giphy.gif",
               "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTNzNnNncmE4ZTliMDg5dmFoN2cxdjduc2dvYWVlM3I4eDRkenp2MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eoszP5cFlchhLIAv2t/giphy.gif"]
    image = random.choice(gifList)
    return f"""
<h1> You Got it !!!! Congratulations </h1>
<img src={image} alt='lower_number'>
"""

@app.route("/<int:num>")
def play(num):
    if num < randomNumber:
        return lower()
    elif num > randomNumber:
        return higher()
    else:
        return correct()

if __name__ == "__main__":
    app.run(debug = True)