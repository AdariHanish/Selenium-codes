#javascript ececution of code(getting the webelement)
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
x = r"c:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(x), options=Options())
driver.execute_script("window.open('https://www.rcvacademy.com/', '_self');")
driver.maximize_window()
time.sleep(5)
a = driver.execute_script('return document.getElementsByTagName("a")[75];')
driver.execute_script("arguments[0].click();", a)
print(driver.title)
time.sleep(5)
driver.quit()