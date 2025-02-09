import requests

APP_ID = "e647af25"
EXERCISE_KEY = "0fd018293b878a7ef8617d9ba6179b78"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

DETAILS = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': EXERCISE_KEY
}

exerciRecord = input("Enter the exercise details: ")

exerciseStats = requests.post(url = API_ENDPOINT, json = {"query": exerciRecord}, headers = DETAILS)
exerciseStats.raise_for_status()
exerciseData = exerciseStats.json()
print(exerciseData)