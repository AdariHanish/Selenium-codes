#click the driver back button
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
x=r"c:\chromedriver\chromedriver.exe"
service=Service(x)
options=Options()
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://youtube.com")
driver.back()