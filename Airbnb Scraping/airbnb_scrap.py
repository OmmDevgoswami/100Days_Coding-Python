from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_option)
driver.get("https://www.airbnb.co.in/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)

location = driver.find_element(By.NAME, "query")
location.send_keys("Bhubaneswar, Odisha")
time.sleep(10)

serach = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[5]/div[2]/div[2]/button')
serach.click()
time.sleep(10)

for _ in range(1,3 ):
    property = driver.find_element(By.XPATH, f"/html/body/div[5]/div/div/div[1]/div/div[3]/div[1]/main/div[2]/div/div[2]/div/div/div/div/div/div[{_}]/div/div[2]/div/div/div/div")
    property.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    url = driver.current_url
    # website = requests.get(url)
    # website.raise_for_status()
    # content = website.text
    time.sleep(5)
    content = driver.page_source
    
    soupDetails = BeautifulSoup(markup = content, features = "html.parser")
    name = soupDetails.find("h1")
    print(name.text)
    
    price = soupDetails.find(class_ = "_hb913q")
    print(price.text)
    
    rating = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[1]/div/div[2]/div/div/div/a/div/div[2]/div[1]')
    print(rating.text)
    
    driver.close()
    driver.switch_to.window(windows[0])
