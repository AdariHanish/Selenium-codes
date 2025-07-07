#find element by partial link teext
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
x = r"C:\chromedriver\chromedriver.exe"
service = Service(x)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
# Open YouTube
driver.get("https://www.amazon.in")
driver.maximize_window()
# Find the search bar and enter the text
p = "Se"
search_button = driver.find_element(By.PARTIAL_LINK_TEXT, p)
search_button.click()
time.sleep(5)
print(driver.title)
driver.quit()