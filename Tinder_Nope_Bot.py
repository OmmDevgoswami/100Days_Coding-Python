"""
Login need to be done manually as their is a captcha adn opt authentication

AS Tinder hasa strong bot detetction, it changes element from time to time
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_option)
driver.get("https://tinder.com/")
driver.maximize_window()

logIn = driver.find_element(By.XPATH, '//*[@id="s187265716"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]')
logIn.click()
time.sleep(2)
try:
    phoneLogin = driver.find_element(By.XPATH, '//*[@id="o-1052973847"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]')
    phoneLogin.click()
    time.sleep(2)
    phoneNumber = driver.find_element(By.NAME, "phone_number")
    phoneNumber.send_keys("8249100154", Keys.ENTER)
    time.sleep(90)#Time for Captcha and OTP Verification
except NoSuchElementException as e:
    moreOption = driver.find_element(By.XPATH, '//*[@id="s408606152"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button')
    moreOption.click()
    time.sleep(2)
    phoneLogin = driver.find_element(By.XPATH, '//*[@id="s408606152"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]')
    phoneLogin.click()
    time.sleep(2)
    phoneNumber = driver.find_element(By.NAME, "phone_number")
    phoneNumber.send_keys("8249100154", Keys.ENTER)
    time.sleep(90)

allow = driver.find_element(By.XPATH, '//*[@id="s408606152"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
allow.click()
print("I am okay")
allowButton = driver.find_element(By.XPATH, '//*[@id="s408606152"]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
allowButton.click()
time.sleep(2)
notificationButton = driver.find_element(By.XPATH, '//*[@id="s408606152"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]/div')
notificationButton.click()
print("I passed")

body = driver.find_element(By.TAG_NAME, "body")

for _ in range(10):
    time.sleep(30)
    # nope = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Nope")]')
    body.send_keys(Keys.ARROW_LEFT)
    print("Nope Done")
    