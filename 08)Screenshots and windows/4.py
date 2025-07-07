#how to handle multiple windows
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
r = r'c:\chromedriver\chromedriver.exe'
service = Service(r)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://yatra.com")
# gives the unique id of the current window
parent = driver.current_window_handle
driver.maximize_window()
print(parent)
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[4]/div[1]/span[1]").click()
all = driver.window_handles
for window in all:
    if window != parent:
        driver.switch_to.window(window)
        print(driver.title)
        driver.maximize_window()
        print(driver.title)
        driver.find_element(By.CLASS_NAME, "twitterOffer offer-sprite").click()
        driver.close()
driver.switch_to.window(parent)
print(driver.title)
time.sleep(20)