# import requests
# import datetime as dt
# from twilio.rest import Client

# API_ENDPOINT = "http://api.weatherapi.com/v1/forecast.json" #Forecast Weather
# KEY = "fed9cc83b6b241a380c185639250502"
# LOCATION = "Bhubaneswar"
# account_sid = "ACbf869a652ff706b05bd37312c9187946"
# auth_token = "700332e4e579ba21013436ab351c8605"


# PARAMETER = {
#     "key" : KEY,
#     "q" : LOCATION,
#     "aqi" : "no"
# }

# weather_details = requests.get(url = API_ENDPOINT, params = PARAMETER)
# weather_details.raise_for_status()
# currentWeather = weather_details.json()

# printDetails = f"""Location: {currentWeather["location"]["name"]}, {currentWeather["location"]["region"]}, {currentWeather["location"]["country"]} 
# Latitude: {currentWeather["location"]["lat"]}  Longitude: {currentWeather["location"]["lon"]}
# Timezone: {currentWeather["location"]["tz_id"]} 
# Temperature: {currentWeather["current"]["temp_c"]}°C or {currentWeather["current"]["temp_f"]}°F
# Feels like: {currentWeather["current"]["feelslike_c"]}°C or {currentWeather["current"]["feelslike_f"]}°F
# Current Condition: {currentWeather["current"]["condition"]["text"]}
# Wind Intensity: {currentWeather["current"]["wind_mph"]}mph or {currentWeather["current"]["wind_kph"]}kph, Direction: {currentWeather["current"]["wind_dir"]}
# Humidity: {currentWeather["current"]["humidity"]}%

# Forcast Details for next 12 hours:
# Date : {currentWeather["forecast"]["forecastday"][0]["date"]}
# """
# print(printDetails)

# time = dt.datetime.now()
# hourCheck = time.hour
# futureHour = hourCheck + 12
# # print(hourCheck)

# prev_condition = None
# start_time = None
# client = Client(account_sid, auth_token)

# for i in range(hourCheck, futureHour + 1):
#     time_check = int(currentWeather["forecast"]["forecastday"][0]["hour"][i]["time"].split(" ")[1].split(":")[0])
#     sky_condition = currentWeather["forecast"]["forecastday"][0]["hour"][i]["condition"]["text"]
#     if currentWeather["forecast"]["forecastday"][0]["hour"][i]["will_it_rain"] == 1:
#         message = client.messages.create(
#                                         body =f"""The Sky seems {sky_condition} at {time_check}:00 hours
#                                         Rain expected !! Be Sure to Carry an Umbrella Please !!""",
#                                         from_='+15075015098',
#                                         to='+919438572321'
#                                     )
#         print(f"The Sky seems {sky_condition} at {time_check}:00 hours")
#         print("Rain expected !! Be Sure to Carry an Umbrella Please !!")
#     else:
#         if prev_condition is None:
#             prev_condition = sky_condition
#             start_time = time_check
#         elif sky_condition != prev_condition:
#             message = client.messages.create(
#                                         body =f"""The Sky seems {prev_condition} from {start_time}:00 to {futureHour}:00 hours. Have a great day!""",
#                                         from_='+15075015098',
#                                         to='+919438572321'
#                                     )
#             print(f"The Sky seems {prev_condition} from {start_time}:00 to {time_check - 1}:00 hours. Have a great day!")
#             prev_condition = sky_condition
#             start_time = time_check

# if prev_condition:
#     message = client.messages.create(
#                                         body =f"""The Sky seems {prev_condition} from {start_time}:00 to {futureHour}:00 hours. Have a great day!""",
#                                         from_='+15075015098',
#                                         to='+919438572321'
#                                     )
#     print(f"The Sky seems {prev_condition} from {start_time}:00 to {futureHour}:00 hours. Have a great day!")