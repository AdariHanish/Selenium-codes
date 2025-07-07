from selenium import webdriver
import time
driver=webdriver.Chrome(Executable_path="C:\chromedriver\chromedriver-win64")
driver.get("https://www.youtube.com")
print(driver.title)
time.sleep(5)
driver.close()