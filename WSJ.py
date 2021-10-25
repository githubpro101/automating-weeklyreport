from selenium import webdriver
import csv

driver = webdriver.Chrome(executable_path=r'C:\Users\Jarvis\Desktop\New folder\Python\selenium\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.wsj.com/market-data/quotes/AAPL/financials/annual/income-statement")
driver.implicitly_wait(10)
year1=driver.find_element_by_xpath('//table[@class="cr_dataTable"]/tbody[1]/tr[1]/td[6]').get_attribute('innerHTML')
year2=driver.find_element_by_xpath('//table[@class="cr_dataTable"]/tbody[1]/tr[1]/td[5]').get_attribute('innerHTML')
year3=driver.find_element_by_xpath('//table[@class="cr_dataTable"]/tbody[1]/tr[1]/td[4]').get_attribute('innerHTML')
year4=driver.find_element_by_xpath('//table[@class="cr_dataTable"]/tbody[1]/tr[1]/td[3]').get_attribute('innerHTML')
year5=driver.find_element_by_xpath('//table[@class="cr_dataTable"]/tbody[1]/tr[1]/td[2]').get_attribute('innerHTML')

revenue=year1,year2,year3,year4,year5

f=open('test.csv','w')
writer=csv.writer(f)
writer.writerow(revenue)
f.close()

#look at DebanjanB's response on https://stackoverflow.com/questions/12325454/how-to-get-text-of-an-element-in-selenium-webdriver-without-including-child-ele
#on the matter of get attribute. Without it, it doesnt work but I still dont know what it does, figure it out later.  
