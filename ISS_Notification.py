import requests
import smtplib
import datetime as dt

MY_LATITUDE = 20.248581
MY_LONGITUDE = 85.796921
LOCATION = "Asia/Kolkata"
MY_EMAIL = "ommdevgoswami01@gmail.com"
MY_PASSWORD = "xozz sqdf dpvy lxqs"

def overall_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    response.raise_for_status()
        
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    # print((latitude, longitude))
    
    if (MY_LATITUDE-5 < latitude and latitude < MY_LATITUDE+5) and (MY_LONGITUDE-5 < longitude and longitude < MY_LONGITUDE+5):
        return True
    else:
        return False
    
# print(overall_location())
format = {
    "lat" : MY_LATITUDE,
    "lng" : MY_LONGITUDE,
    "tzid" : LOCATION,
    "formatted" : 0
}

sunTime = requests.get(url="https://api.sunrise-sunset.org/json", params=format)
sunTime.raise_for_status()
sunTiming = sunTime.json()

sunRise = int(sunTiming["results"]["sunrise"].split("T")[1].split(":")[0])
sunSet = int(sunTiming["results"]["sunset"].split("T")[1].split(":")[0])

Now = dt.datetime.now()
timeNow = Now.hour

if sunRise>timeNow or timeNow>sunSet:
    print("It is night")
    if overall_location():
        print("The ISS is above your location")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, 
                                to_addr=MY_EMAIL,
                                msg="Subject: Look Up! \n\n The ISS is above your location.")
    else:
        print("The ISS is not above your location")
else:
    print("It is day")