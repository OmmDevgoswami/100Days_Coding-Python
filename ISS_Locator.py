import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
response.raise_for_status()
    
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

location = (latitude, longitude)

print(location)