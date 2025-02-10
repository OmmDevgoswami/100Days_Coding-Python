import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

telegram_key = os.getenv("TELEGRAM_KEY")
botID = os.getenv("BOT_ID")

def telegram_bot_sendtext(bot_message):
    
    bot_token = telegram_key
    bot_chatID = botID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

SHEETY_ENDPOINT = "https://api.sheety.co/f50c3ef24829fd6933e9ea5e8e6fcaa5/flightDetails/sheet1"
AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

AUTHENTICATION = {
    "Authorization": os.getenv("SHEETY_AUTH"),
    "Content-Type": "application/json"
}

API_KEY =  os.getenv("AMADEUS_KEY")
API_SECRET = os.getenv("AMADEUS_SECRET")

MY_LOCATION_IATA = "CCU"
CURRENCY = "INR"
LOCATION = "Kolkata"

sheets = requests.get(url=SHEETY_ENDPOINT, headers=AUTHENTICATION)
sheets.raise_for_status()
sheetData = sheets.json()["sheet1"]

auth_response = requests.post(
    "https://test.api.amadeus.com/v1/security/oauth2/token",
    data={
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    }
)
access_token = auth_response.json().get("access_token")
HEADER = {
    "Authorization": f"Bearer {access_token}"
}

today = dt.datetime.today()
start_date = today + dt.timedelta(days=1)

for destination in sheetData:
    DESTINATION_IATA = destination["iataCode"]
    RADIUS_AMOUNT = destination["price"]
    print(f"\nChecking flights for: {destination['city']} ({DESTINATION_IATA})")

    for days in range(1, 5):
        departure_date = (start_date + dt.timedelta(days=days)).strftime('%Y-%m-%d')

        params = {
            "originLocationCode": MY_LOCATION_IATA,
            "destinationLocationCode": DESTINATION_IATA,
            "departureDate": departure_date,
            "adults": 1,
            "max": 5,
            "currencyCode": CURRENCY  
        }

        response = requests.get(url=AMADEUS_ENDPOINT, headers=HEADER, params=params)
        response.raise_for_status()
        flights_data = response.json()

        print(f"\nFlights on {departure_date}:")
        if "data" in flights_data:
            for offer in flights_data["data"]:
                price_inr = float(offer["price"]["total"])  
                airline = offer["validatingAirlineCodes"][0]
                
                if price_inr <= RADIUS_AMOUNT:
                    print(f"- {airline}: ₹{price_inr} (Under ₹{RADIUS_AMOUNT}) ✅")
                    telegram_bot_sendtext(f"""✈️ Low price alert! {airline} flight to {destination['city']} from {LOCATION} for ₹{price_inr} on {departure_date}""")
                else:
                    print(f"- {airline}: ₹{price_inr} ❌ (Too Expensive)")
        else:
            print("No flights found")
