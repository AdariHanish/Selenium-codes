#find element by css selector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
x=r"c:\chromedriver\chromedriver.exe"
service=Service(x)
options=Options()
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://youtube.com")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search']").send_keys("ninila").click()#enters the text ninila in the search box and press enter
time.sleep(10)
print(driver.title)
driver.quit()