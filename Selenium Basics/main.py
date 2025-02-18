from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True) #To keep the wbsite open

driver = webdriver.Chrome(options = chrome_option)
driver.get("https://www.python.org/")

# driver.close() #Closes the tab as soon as it opens
# driver.quit() #Closes the whole chrome program (i.e, If multiple tabs are opened)