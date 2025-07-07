#how to check if the element is enabled or not
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
x=r"c:\chromedriver\chromedriver.exe"
service=Service(x)
options=Options()
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://youtube.com")
search=driver.find_element(By.XPATH,"//input[@placeholder='Search']").is_enabled()
print(search)
driver.quit()