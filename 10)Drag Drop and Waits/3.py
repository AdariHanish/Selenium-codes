#implicit wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
x=r"c:\chromedriver\chromedriver.exe"
service = Service(x)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.youtube.com")
driver.maximize_window()
time.sleep(5)#hard wait
driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("selenium")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[@title='Search']//yt-icon//div").click() #element is found so it wont wait for 10 sec
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"ajffs").click() #waits for 10 sec and then it will give output as its invalid xpath
time.sleep(5)
driver.quit()