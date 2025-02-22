""" 
Following Accounts Lead to Restriction under the rules of Instagram.
"""

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# import time
# import os
# from dotenv import load_dotenv

# load_dotenv()

# EMAIL = os.getenv("EMAIL")
# PASSKEY = os.getenv("PASSWORD")

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options = chrome_option)
# driver.get("https://www.instagram.com/accounts/login/?hl=en")
# driver.maximize_window()
# time.sleep(5)

# try:
#     username = driver.find_element(By.NAME, "username")
#     username.send_keys(EMAIL)
#     time.sleep(5)
#     password = driver.find_element(By.NAME, "password")
#     password.send_keys(PASSKEY, Keys.ENTER)
#     time.sleep(5)
# except NoSuchElementException as e:
#     username = driver.find_element(By.XPATH, '//*[@id=":r6:"]')
#     username.send_keys(EMAIL)
#     time.sleep(5)
#     password = driver.find_element(By.XPATH, '//*[@id=":r9:"]')
#     password.send_keys(PASSKEY, Keys.ENTER)
#     time.sleep(5)

# time.sleep(15)
# # try:
# #     closerPopUp = driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div[2]/div/div')
# #     closerPopUp.click()
# # except NoSuchElementException as e:
# #     e
# # time.sleep(5)

# # Need to Manually click "Not Now"

# searchOption = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span")
# searchOption.click()
# time.sleep(10)
# searchBar = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
# searchBar.send_keys("flowers_india_")
# time.sleep(10)
# option = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div')
# option.click()
# time.sleep(10) 

# followers = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
# followers.click()
# time.sleep(15)

# for _ in range(2, 11):
#     button = driver.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{_}]/div/div/div/div[3]/div/button')
#     button.click()
#     time.sleep(5)
#     print("Followed")