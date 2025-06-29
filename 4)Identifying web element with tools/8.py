#getting element list
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
x=r"c:\chromedriver\chromedriver.exe"
service=Service(x)
options=Options()
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(5)
search_button=driver.find_elements(By.TAG_NAME,"yt-formatted-string")
print(len(search_button))
for i in search_button:
    print(i.text)
time.sleep(5)
driver.quit()