from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_option)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookieClicker = driver.find_element(By.CSS_SELECTOR, "#cookie")
startTime = time.time()
finishTime = float(input("How many minutes do you wish to run the Cookie Clicker: "))*60
lastCheck = startTime

buyableOptions = ['//*[@id="buyCursor"]/b', '//*[@id="buyGrandma"]/b', '//*[@id="buyFactory"]/b', 
                  '//*[@id="buyMine"]/b', '//*[@id="buyShipment"]/b', '//*[@id="buyAlchemy lab"]/b', 
                  '//*[@id="buyPortal"]/b', '//*[@id="buyTime machine"]/b']
maxValues = []
for items in buyableOptions:
    values = driver.find_element(By.XPATH, items)
    val = values.text.split()
    maxValues.append(val[len(val) - 1].replace(",", ""))

while time.time() - startTime <= finishTime:
    cookieClicker.click()
    noOfScore = driver.find_element(By.CSS_SELECTOR, "#money")
    scoreVal = int(noOfScore.text.replace(",",""))
    
    if time.time() - lastCheck >= 5:
        affordable = [int(val) for val in maxValues if scoreVal >= int(val)]

        if affordable: 
            buyOption = max(affordable)
            feature = driver.find_element(By.XPATH, buyableOptions[maxValues.index(str(buyOption))])
            feature.click()
        lastCheck = time.time()
        
scorePerSecond = driver.find_element(By.CSS_SELECTOR, "#cps")
value = scorePerSecond.text.split()
print(f"Score Per Second after {finishTime} seconds is {value[len(value) - 1]}")