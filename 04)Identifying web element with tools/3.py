#find element by xpath
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
driver.find_element(By.XPATH,"/html[1]/body[1]/ytd-app[1]/div[1]/div[2]/ytd-masthead[1]/div[4]/div[2]/yt-searchbox[1]/div[1]/form[1]/input[1]").send_keys("ninila").click()#enters the text ninila in the search box and press enter
time.sleep(10)
print(driver.title)
driver.quit()