import requests

API_ENDPOINT = "http://api.weatherapi.com/v1/current.json" #Current Weather
KEY = "fed9cc83b6b241a380c185639250502"
LOCATION = "Bhubaneswar"

PARAMETER = {
    "key" : KEY,
    "q" : LOCATION,
    "aqi" : "no"
}

weather_details = requests.get(url = API_ENDPOINT, params = PARAMETER)
weather_details.raise_for_status()
currentWeather = weather_details.json()

# print(currentWeather)

printDetails = f"""Location: {currentWeather["location"]["name"]}, {currentWeather["location"]["region"]}, {currentWeather["location"]["country"]} 
Latitude: {currentWeather["location"]["lat"]}  Longitude: {currentWeather["location"]["lon"]}
Timezone: {currentWeather["location"]["tz_id"]} 
Temperature: {currentWeather["current"]["temp_c"]}°C or {currentWeather["current"]["temp_f"]}°F
Feels like: {currentWeather["current"]["feelslike_c"]}°C or {currentWeather["current"]["feelslike_f"]}°F
Current Condition: {currentWeather["current"]["condition"]["text"]}
Wind Intensity: {currentWeather["current"]["wind_mph"]}mph or {currentWeather["current"]["wind_kph"]}kph, Direction: {currentWeather["current"]["wind_dir"]}
Humidity: {currentWeather["current"]["humidity"]}%
"""

print(printDetails)