from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_option)
driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account?trk=guest_homepage-basic_nav-header-signin")
driver.maximize_window()

name = driver.find_element(By.NAME, "session_key")
name.send_keys("ayamamouto@gmail.com")
time.sleep(10)

password  = driver.find_element(By.NAME, "session_password")
password.send_keys("password2321")
time.sleep(5)

signIn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
signIn.click()
time.sleep(5)

jobSection = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
jobSection.click()
time.sleep(5)

position = driver.find_element(By.CSS_SELECTOR, "input.jobs-search-box__text-input")
position.send_keys("Python Developer")
time.sleep(2)
position.send_keys(Keys.ENTER)
# location = driver.find_element(By.XPATH, "//input[contains(@id, 'jobs-search-box-location')]")
# location.send_keys("India")
time.sleep(2)
easyApply = driver.find_element(By.CSS_SELECTOR, "#searchFilter_applyWithLinkedin")
easyApply.click()
time.sleep(2)
search = driver.find_element(By.CSS_SELECTOR, "button.jobs-search-box__submit-button")
search.click()
time.sleep(5)

saveButton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/button')
saveButton.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
followButton = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/section/section/div[1]/div[1]/button')
followButton.click()

# checkText = driver.find_element(By.CSS_SELECTOR, 'span[dir="ltr"]')
# if checkText.text == "Easy Apply":
#     saveButton = driver.find_element(By.CSS_SELECTOR, "jobs-save-button__text")
#     for _ in saveButton:
#         _.click()
#         saveButton.remove(_)
        