#screenshot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")
driver.maximize_window()
driver.get_screenshot_as_file("screenshot.png")
driver.save_screenshot(r"C:\Users\honey\Desktop\Selenium pin to pin codes\8)Screenshots and windows\screenshot2.png")
time.sleep(5)
print(driver.title)
driver.quit()