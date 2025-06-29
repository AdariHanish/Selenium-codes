#how to get text of an element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
x=r"c:\chromedriver\chromedriver.exe"
service=Service(x)
options=Options()
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://youtube.com")
driver.find_element(By.XPATH,"//yt-formatted-string[text()='Sign in']").click()
print(driver.find_element(By.XPATH,"//yt-formatted-string[text()='Sign in']").text)