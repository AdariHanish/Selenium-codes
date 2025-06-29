#handing autosugessions
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
x = r"C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(x), options=Options())
driver.get("https://www.flipkart.com")
driver.maximize_window()
# Send keys to search bar
d = driver.find_element(By.NAME, "q")
d.send_keys("samsung Galaxy")
time.sleep(2)
# Get suggestions
b = driver.find_elements(By.XPATH, "//ul[@class='_1sFryS _2x2Mmc _3ofZy1']/li")
print(len(b))
for i in b:
    if "Samsung Galaxy book 4" in i.text:
        i.click()
        time.sleep(5)
        break
d.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()