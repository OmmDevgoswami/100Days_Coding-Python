from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_option)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Omm")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Devgoswami")
email = driver.find_element(By.NAME, "email")
email.send_keys("teamuniverse.omm@gmail.com")
button = driver.find_element(By.TAG_NAME, "button").submit()

"""Yaahoooo First from filled"""