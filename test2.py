from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r'C:\Users\Jarvis\Desktop\New folder\Python\selenium\chromedriver.exe')
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.implicitly_wait(10)
driver.find_element_by_id("datepicker").click()