#handling the slider
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
r = r'c:\chromedriver\chromedriver.exe'
service = Service(r)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.snapdeal.com/products/electronics-home-audio-systems?sort=plrty")
driver.maximize_window()
left = driver.find_element(By.XPATH, "//a[contains(@class,'left-handle')]")
right = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")
a = ActionChains(driver)
a.drag_and_drop_by_offset(left, 0, 50).perform()
time.sleep(5)
a.click_and_hold(right).move_by_offset(-50, 0).release().perform()
time.sleep(5)
driver.quit()