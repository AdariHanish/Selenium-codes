#how to handle alerts in python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
r = r'c:\chromedriver\chromedriver.exe'
service = Service(r)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH, "/html/body/button").click()
print(driver.switch_to.alert.text)
time.sleep(3)
driver.switch_to.alert.send_keys("hello")
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/button").click()
driver.switch_to.alert.dismiss()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(3)
print(driver.title)
driver.close()