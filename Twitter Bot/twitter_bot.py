from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSKEY = os.getenv("PASSWORD")

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options = self.chrome_option)
        
    def get_internet_speed(self):
        time.sleep(5)
        self.driver.get("https://www.speedtest.net/")
        continueButton = self.driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
        continueButton.click()
        time.sleep(5)
        goButton = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        goButton.click()
        time.sleep(60)
        upTime = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        downTime = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        message = f"""BSNL - 1800 Monthly Plan Truth
Up Time / Download Time: {upTime.text}
Down Time / Upload Time: {downTime.text}"""
        return message
       
    def tweetMessage(self, twitt):
        self.driver.get("https://x.com")
        self.driver.maximize_window()

        time.sleep(10)
        logIn = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
        logIn.click()
        time.sleep(90) #Long Page Loading

        emailId = self.driver.find_element(By.NAME, "text")
        emailId.send_keys(EMAIL)
        time.sleep(3)
        emailId.send_keys(Keys.ENTER)
        time.sleep(10)
        try:
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys(PASSKEY)
            time.sleep(3)
            password.send_keys(Keys.ENTER)
        except NoSuchElementException as e:
            userNameCheck = self.driver.find_element(By.NAME, "text")
            userNameCheck.send_keys("@Unshared_Voice")
            time.sleep(3)
            userNameCheck.send_keys(Keys.ENTER)
            time.sleep(10)
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys("password@2321")
            time.sleep(3)
            password.send_keys(Keys.ENTER)
        time.sleep(20)

        message = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/span')
        message.send_keys(twitt)
        time.sleep(5)
        postButton = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        postButton.click()
        
botTest = InternetSpeedTwitterBot()
value = botTest.get_internet_speed()
print(value)
botTest.tweetMessage(value)
print("Message Printed successfully !!")