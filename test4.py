from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date
today = date.today().day
# todaysdate = today.strftime("%m/%d/%y")
datenow=str(today)
driver = webdriver.Chrome(executable_path=r'C:\Users\Jarvis\Desktop\New folder\Python\selenium\chromedriver.exe')
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.implicitly_wait(10)
elem=driver.find_element_by_id("datepicker")
elem.click()
alldates=driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//a")
for dateelement in alldates:
    todaydate=dateelement.text
    if todaydate==datenow:
        dateelement.click()
        break
    

