#perform drag and drop
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
x = r"c:\chromedriver\chromedriver.exe"
service = Service(x)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.w3schools.com/html/html5_draganddrop.asp")
source = driver.find_element(By.ID, "drag1")
target = driver.find_element(By.ID, "div1")
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()
time.sleep(5)
driver.quit()