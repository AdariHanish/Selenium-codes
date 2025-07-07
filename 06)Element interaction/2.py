#Handling hidden elements
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
x=r"c:\chromedriver\chromedriver.exe"
service=Service(x)
options=Options()
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
driver.maximize_window()
time.sleep(3)
button=driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']")
element=driver.find_element(By.XPATH,"//div[@id='myDIV']")
button.click()
print(element.is_displayed())
button.click()
print(element.is_displayed())
driver.quit()