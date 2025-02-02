import requests

MY_LATITUDE = 20.248581
MY_LONGITUDE = 85.796921
LOCATION = "Asia/Kolkata"

location = {
    "lat" : MY_LATITUDE,
    "lng" : MY_LONGITUDE,
    "tzid" : LOCATION,
    # "formatted" : 0
}
sunTime = requests.get(url="https://api.sunrise-sunset.org/json", params=location)
sunTime.raise_for_status()
sunTiming = sunTime.json()

sunRise = sunTiming["results"]["sunrise"]
sunSet = sunTiming["results"]["sunset"]
timeZone = sunTiming["tzid"]
print(f"Sun Rise Timing: {sunRise}\nSun Set Timing: {sunSet}\nTime Zone: {timeZone}")
# print(sunRise)