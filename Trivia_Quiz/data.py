import requests

QUESTION = 20
CATEGORY = 27
TYPE = "boolean"

Parameter = {
    "amount": QUESTION,
    "category" : CATEGORY,
    "type" : TYPE
}

data = requests.get(url="https://opentdb.com/api.php", params=Parameter)
data.raise_for_status()
question = data.json()

question_data = question["results"]