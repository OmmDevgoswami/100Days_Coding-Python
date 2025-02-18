from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_option)
driver.get("https://www.python.org/")

upcomingEvents = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

events = {}
currentEvent = [_.text.splitlines() for _ in upcomingEvents]

for _ in range(len(currentEvent)):
    events[_] = {"Time": currentEvent[_][0] ,
                 "Name" : currentEvent[_][1]}

print(events)
driver.quit()