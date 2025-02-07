import requests
import datetime as dt
import os
from dotenv import load_dotenv
import pytz

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API = "https://www.alphavantage.co/query" #25 requests per day
NEWS_API = "https://newsapi.org/v2/everything"

telegram_key = os.getenv("TELEGRAM_KEY")
botID = os.getenv("BOT_ID")
STOCK_API_KEY = os.getenv("STOCK_KEY")
NEWS_API_KEY = os.getenv("NEWS_KEY")

usa_tz = pytz.timezone('America/New_York')
news_yesterday = str(dt.datetime.now(usa_tz).date() - dt.timedelta(days = 2))

STOCK_PARAMETER = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY
}

NEWS_PARAMETER = {
    "q" : COMPANY_NAME,
    "from" : news_yesterday,
    "sortBy" : "popularity",
    "apiKey" : NEWS_API_KEY
}

STOCK_Deatils = requests.get(url = STOCK_API, params = STOCK_PARAMETER)
STOCK_Deatils.raise_for_status()
stockData = STOCK_Deatils.json()

NEWS_Deatils = requests.get(url = NEWS_API, params = NEWS_PARAMETER)
NEWS_Deatils.raise_for_status()
newsData = NEWS_Deatils.json()

stockDetails = f"""Stock Name: {stockData["Meta Data"]["2. Symbol"]} 
Date: {stockData["Meta Data"]["3. Last Refreshed"]}
Type: {stockData["Meta Data"]["4. Output Size"]}
Time Zone: {stockData["Meta Data"]["5. Time Zone"]}"""
print(stockDetails)

today = stockData["Meta Data"]["3. Last Refreshed"]
yesterday = str((dt.datetime.strptime(today, "%Y-%m-%d") - dt.timedelta(days = 1)).strftime("%Y-%m-%d"))
print("\n",today, yesterday)

todaysOpening = float(stockData["Time Series (Daily)"][today]["1. open"])
yesterdaysOpening = float(stockData["Time Series (Daily)"][yesterday]["1. open"])
percentage = round(((todaysOpening - yesterdaysOpening) / yesterdaysOpening) * 100, 2)

val = 0
emoji = ""
alert = ""

if percentage > 0:
    emoji = "🔺"
    val = abs(percentage)
    alert = f"{STOCK}: {emoji} {val}%"
else:
    emoji = "🔻"
    val = abs(percentage)
    alert = f"{STOCK}: {emoji} {val}%"

news_details = []
for _ in range(3):
    news_details.append(f""""Headline": {newsData["articles"][_]["title"]}
"Description": {newsData["articles"][_]["description"]}
    -By {newsData["articles"][_]["source"]["name"]}""")

print("\n",news_details)

def telegram_bot_sendtext(bot_message):
    
    bot_token = telegram_key
    bot_chatID = botID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

message = telegram_bot_sendtext(f"""{alert}
{news_details[0]}\n
{news_details[1]}\n
{news_details[2]}""")