from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

telegram_key = os.getenv("TELEGRAM_KEY")
botID = os.getenv("BOT_ID")
email = "ommdevgoswami01@gmail.com"
password = os.getenv("PASSWORD")

URL = "https://www.amazon.in/gp/product/B0CQXMXJC5?smid=A1KZCGRGYHBO6U&th=1"

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6"
}
website = requests.get(URL, headers = header)
website.raise_for_status()
content = website.text

soupDeatails = BeautifulSoup(markup = content, features = "html.parser")
# print(soupDeatails.prettify())
price = soupDeatails.select_one("span.a-offscreen")
checkPrice = float(price.text.split("₹")[1].replace(",", ""))

name = soupDeatails.select_one("span#productTitle")
name = name.text.strip()
print(name)

def telegram_bot_sendtext(bot_message):
    
    bot_token = telegram_key
    bot_chatID = botID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    
    response = requests.get(send_text)
    return response.json()

tragetPrice = 3900
if checkPrice <= tragetPrice:
    message = f"""
SALE SALE SALE ‼️⚜️

Price Sale alert: {price.text}

Product Name: {name}

Site link : {URL}"""
    telegram_bot_sendtext(message)
    with smtplib.SMTP("smtp.gmail.com", port=587) as mail:
        mail.starttls()
        mail.login(user = email, password = password)
        mail.sendmail(
            from_addr = email,
            to_addrs = email,
            msg=f"Subject:Price Alert\n\n{message}".encode('utf-8')
    )    
    print("Price is less than or equal to target price")
else:
    print("Scrap again tomorrow")