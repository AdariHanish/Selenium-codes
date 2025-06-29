#how to execute the javascript code(opening the browser)
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
x = r"c:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(x), options=Options())
driver.execute_script("window.open('https://www.rcvacademy.com/', '_self');")
driver.maximize_window()
time.sleep(5)
print(driver.title)
driver.quit()