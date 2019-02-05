
from selenium import webdriver
driver= webdriver.Chrome("C:\\Users\\user\\Downloads\\chromedriver.exe")
p1=driver.get('https://www.codechef.com/contests')
## Present Contests
table = driver.find_element_by_xpath("//table[@class='dataTable']")
print(table.text)
