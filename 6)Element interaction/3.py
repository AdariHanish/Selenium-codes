#handling the checkboxes
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
x = r"c:\chromedriver\chromedriver.exe"
service = Service(x)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window
driver.get("https://www.ironspider.ca/forms/checkradio.htm")
driver.maximize_window
time.sleep(5)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/blockquote[1]/form[1]/input[1]").click()
time.sleep(5)
print(driver.title)
driver.quit()