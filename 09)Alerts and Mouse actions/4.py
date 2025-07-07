#performing double click
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
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
x = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
time.sleep(5)
a = ActionChains(driver)
time.sleep(4)
a.move_to_element(x).double_click().perform()
time.sleep(3)
driver.quit()