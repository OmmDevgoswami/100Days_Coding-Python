from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import smtplib
import urllib.parse
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv("EMAIL_ID")
PASSWORD = os.getenv("PASSKEY")
telegram_key = os.getenv("TELEGRAM_API")
botID = os.getenv("BOT_ID")

class Airbnb_Data:
    def __init__(self, Userlocation, propertyNo, checkIn, checkOut):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options = chrome_option)
        self.driver.get("https://www.airbnb.co.in/")
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(5)

        location = self.driver.find_element(By.NAME, "query")
        location.send_keys(Userlocation)
        time.sleep(10)
        
        checkInDate = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[3]/div[1]/div/div')
        checkInDate.click()
        time.sleep(5)
        date1 = self.driver.find_element(By.CSS_SELECTOR, f'button[data-state--date-string="2025-{checkIn}"]')
        date1.click()
        time.sleep(5)
        
        checkOutDate = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[3]/div[3]/div/div')
        checkOutDate.click()
        time.sleep(5)
        date2 = self.driver.find_element(By.CSS_SELECTOR, f'button[data-state--date-string="2025-{checkOut}"]')
        date2.click()
        time.sleep(10)

        serach = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[5]/div[2]/div[2]/button')
        serach.click()
        time.sleep(10)
        
        self.data = []

        for _ in range(1, propertyNo + 1):
            property = self.driver.find_element(By.XPATH, f"/html/body/div[5]/div/div/div[1]/div/div[3]/div[1]/main/div[2]/div/div[2]/div/div/div/div/div/div[{_}]/div/div[2]/div/div/div/div")
            property.click()
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])

            url = self.driver.current_url
            # website = requests.get(url)
            # website.raise_for_status()
            # content = website.text
            propertyUrl = url
            time.sleep(5)
            content = self.driver.page_source
            
            soupDetails = BeautifulSoup(markup = content, features = "html.parser")
            name = soupDetails.find("h1")
            propertyName = name.text
            
            price = soupDetails.find(class_ = "_hb913q")
            propertyPrice = price.text.strip().replace(",","")
            
            try:
                rating = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[1]/div/div[2]/div/div/div/a/div/div[2]/div[1]')
            except NoSuchElementException as e:
                try:
                    rating = self.driver.find_element(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[3]/div[2]')
                except NoSuchElementException as f:
                    ratingNew = self.driver.find_element(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[3]/a')
                    rating = ratingNew[0]
            propertyRating = rating.text
            
            self.driver.close()
            self.driver.switch_to.window(windows[0])
            self.data.append([propertyName, propertyPrice, propertyRating, propertyUrl])
            
        self.driver.quit()
        
    def propertyDetails(self):
        return self.data

class Messenger:
    def __init__(self, data):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        self.dataDriver = webdriver.Chrome(options = chrome_option)
        self.dataDriver.maximize_window()
        self.data = data
    
    def googleForm(self):
        self.dataDriver.get("https://docs.google.com/forms/d/e/1FAIpQLSfSIEo2E_BGH8Z8Gf6PyUU7wYB5QJjREBpwCG269kfs8hjGMQ/viewform")
        time.sleep(5)
        for _ in self.data:
            propertyName = self.dataDriver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            propertyName.send_keys(_[0])
            propertyPrice = self.dataDriver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            propertyPrice.send_keys(_[1])
            propertyRating = self.dataDriver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            propertyRating.send_keys(_[2])
            propertyUrl = self.dataDriver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
            propertyUrl.send_keys(_[3])
            sendButton = self.dataDriver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            sendButton.click()
            time.sleep(3)
            self.dataDriver.refresh()
            
        self.dataDriver.quit()
            
    def email_(self, email):
        count = 1
        messages = []
        for _ in self.data:
            message = f"""Airbnb Option - {count}
Property Name: {_[0]} has a price of Rs.{str(_[1]).replace("₹", "")} and a Rating of {_[2]}
Link : {_[3]}"""
            messages.append(message)
            count += 1
            
        finalMessage = "\n\n".join(messages)
        
        with smtplib.SMTP("smtp.gmail.com", port = 587) as emailSender:
            emailSender.starttls()
            emailSender.login(user = EMAIL, password = PASSWORD)
            emailSender.sendmail(from_addr = EMAIL,
                                 to_addrs = email,
                                 msg =f"Subject:Airbnb Properties\n\n{finalMessage}"
            )
        
    def telegramBot(self):
        count = 1
        messages = []
        for _ in self.data:
            message = f"""Airbnb Option - {count}
Property Name: {str(_[0]).replace(",", "").replace(":","")} has a price of Rs.{str(_[1]).replace("₹", "")} and a Rating of {_[2]}
Link : {_[3]}"""
            messages.append(message)
            count += 1
            
        finalMessage = "\n\n".join(messages)
        
        encoded_message = urllib.parse.quote(finalMessage)
        send_text = f'https://api.telegram.org/bot{telegram_key}/sendMessage?chat_id={botID}&parse_mode=Markdown&text={encoded_message}'
        response = requests.get(send_text)
        return response.json()

userLocation = "Bhubaneswar, Odisha"
propertyNo = 2
checkIn = "02-28"
checkOut = "03-02"
testCall = Airbnb_Data(userLocation, propertyNo, checkIn, checkOut)
val = testCall.propertyDetails()

sent = Messenger(val)
sent.googleForm()
sent.email_("ommdevgoswami@yahoo.com")
sent.telegramBot()

print("Success")