#simple select autosugession
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
x = r"C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(x))
driver.get("https://www.flipkart.com")
driver.maximize_window()
d = driver.find_element(By.NAME, "q")
d.send_keys("samsung Galaxy S21 Ultra")
d.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()