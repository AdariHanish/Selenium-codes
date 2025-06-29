#how to get element attribute value
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
x=r"c:\chromedriver\chromedriver.exe"
service=Service(x)
options=Options()
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://youtube.com")
driver.maximize_window()
a=driver.find_element(By.ID,"search")
print(a.get_attribute("class"))
print(a.get_attribute("id"))
print(a.get_attribute("type"))