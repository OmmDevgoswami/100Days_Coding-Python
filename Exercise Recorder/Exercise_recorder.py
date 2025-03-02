import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("NURTIONIX_APP_ID")
EXERCISE_KEY = os.getenv("NURTIONIX_KEY")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API = "https://api.sheety.co/f50c3ef24829fd6933e9ea5e8e6fcaa5/copyOfMyWorkouts/workouts"

DETAILS = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': EXERCISE_KEY
}

exerciRecord = input("Enter the exercise details: ")

exerciseStats = requests.post(url = API_ENDPOINT, json = {"query": exerciRecord}, headers = DETAILS)
exerciseStats.raise_for_status()
exerciseData = exerciseStats.json()
# print(exerciseData)

now = dt.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

printDetails = f"""
Date : {date},
Time : {time},
Exercise {exerciseData['exercises'][0]['name'].title()}, 
Duration: {exerciseData['exercises'][0]['duration_min']}, 
Calories: {exerciseData['exercises'][0]['nf_calories']}"""
print(printDetails)

Update_Details = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exerciseData['exercises'][0]['name'].title(),
        "duration": exerciseData['exercises'][0]['duration_min'],
        "calories": exerciseData['exercises'][0]['nf_calories']
    }
}

AUTHENTICATION ={
    "Authorization" : os.getenv("SHEETY_TOKEN"),
    "Content-Type" : "application/json"
}

recorder = requests.post(url = SHEETY_API, json = Update_Details, headers = AUTHENTICATION)
recorder.raise_for_status()
print(recorder.text)