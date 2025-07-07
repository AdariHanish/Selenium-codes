#by class name
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
x = r"C:\chromedriver\chromedriver.exe"
service = Service(x)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.youtube.com")
driver.maximize_window()
time.sleep(3)
search_box = driver.find_element(By.CLASS_NAME, "ytd-searchbox")
search_box.send_keys("Python Programming")
search_button = driver.find_element(By.CLASS_NAME, "style-scope ytd-searchbox")
search_button.click()
time.sleep(5)
print(driver.title)
driver.quit()
