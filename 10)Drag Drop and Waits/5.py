#fluent wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
x=r"c:\chromedriver\chromedriver.exe"
service = Service(x)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
wait=WebDriverWait(driver, 10 , 2,ignored_exceptions=["NoSuchElementException"])#(driver, timeout, poll_frequency, ignored_exceptions)
driver.get("https://www.youtube.com")
driver.maximize_window()
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))).send_keys("selenium")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Search']//yt-icon//div"))).click()
wait.until(EC.presence_of_element_located((By.XPATH, "ajkdf"))).click()#error due to wrong xpath
driver.quit()