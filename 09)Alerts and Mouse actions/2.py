#how to handl the mouse hover
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
x = r"C:\chromedriver\chromedriver.exe"
service = Service(x)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://yatra.com")
driver.maximize_window()
x = driver.find_element(By.XPATH, "//span[contains(text(),'Login / Signup')]")
time.sleep(5)
a = ActionChains(driver)
time.sleep(4)
a.move_to_element(x).click().perform()
time.sleep(3)
driver.find_element(By.XPATH, "//p[normalize-space()='My Bookings']").click()
print(driver.title)
driver.quit()