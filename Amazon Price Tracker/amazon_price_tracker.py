from bs4 import BeautifulSoup
import requests
import smtplib

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6"
}
website = requests.get("https://www.amazon.in/gp/product/B0CQXMXJC5?smid=A1KZCGRGYHBO6U&th=1", headers = header)
website.raise_for_status()
content = website.text

soupDeatails = BeautifulSoup(markup = content, features = "html.parser")
# print(soupDeatails.prettify())
price = soupDeatails.select_one("span.a-offscreen")
checkPrice = float(price.text.split("₹")[1].replace(",", ""))

tragetPrice = 3900
if checkPrice <= tragetPrice:
    print("Price is less than or equal to target price")
else:
    print("Scrap again tomorrow")