from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path=r'C:\Users\Jarvis\Desktop\New folder\Python\selenium\chromedriver.exe')
driver.get('https://www.linkedin.com')
driver.maximize_window()
time.sleep(2)

username=driver.find_element_by_id("session_key")
password=driver.find_element_by_id("session_password")

username.send_keys('frank.won3@gmail.com')
password.send_keys('dnjs2552')
time.sleep(2)

submit=driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

driver.find_element_by_id("ember44").click()
time.sleep(2)

# document=("//button[@class='artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view']")[3]
# time.sleep(2)

# document.click()
# time.sleep(2)