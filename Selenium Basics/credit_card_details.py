from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_option)
driver.get("https://fill.dev/form/credit-card-simple")

name = driver.find_element(By.NAME, "cc-name")
name.send_keys("Omm Devgoswami")
type = driver.find_element(By.NAME, "cc-type").click()
typeClick = driver.find_element(By.CSS_SELECTOR, "option[value='visa']").click()
creditCard = driver.find_element(By.NAME, "cc-number")
creditCard.send_keys("4519-1508-0103")
cvvNo = driver.find_element(By.NAME, "cc-csc")
cvvNo.send_keys("498")

expireMonth = driver.find_element(By.NAME, "cc-exp-month").click()
expireMonthClick = driver.find_element(By.CSS_SELECTOR, "option[value = '2']").click()


expireYear = driver.find_element(By.NAME, "cc-exp-year")
# expireYearClick = driver.find_element(By.CSS_SELECTOR, "option[value = '2028']").click()
select_year = Select(expireYear)
select_year.select_by_value("2028") 

button = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div/div/div/div[2]/form/div[7]/div/button').click()