from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_option)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# value = driver.find_element(By.CSS_SELECTOR, "#articlecount ul li a") #There ware two link with all attributes same so..
value = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
print(f"Total No.of Articles on Wiki is {value.text}")

# value.click() #this function is used to perform the 'click' operation

#linkCLick = driver.find_element(By.LINK_TEXT, "Content portals").click()  #Automatically searches the element and clicks on it

driver.maximize_window() #In minimized version search is replaced by a span so maximise it 
searchBar = driver.find_element(By.NAME, "search")
searchBar.send_keys("Python", Keys.ENTER) 
""" send_keys : Let's use dirctly type inside a input field 
'Keys' keyword is used to use various keyword buttons such an enter, shift, etc.
"""

# driver.quit()