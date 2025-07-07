#to know about the current working url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
x=r"c:\chromedriver\chromedriver.exe"
service=Service(x)
options=Options()
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://youtube.com")
print(driver.current_url)