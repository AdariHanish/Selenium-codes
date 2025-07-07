#performing the right click
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
x = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
time.sleep(5)
a = ActionChains(driver)
time.sleep(4)
a.context_click(x).perform()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Copy']").click()
print(driver.title)
driver.quit()