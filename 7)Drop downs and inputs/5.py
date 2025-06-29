#how to handle calender
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
driver.find_element(By.ID, "datepicker").click()
while True:
    month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
    if month == "August" and year == "2025":
        break
    driver.find_element(By.CLASS_NAME, "ui-datepicker-next").click()
    time.sleep(0.2)
driver.find_element(By.XPATH, "//a[text()='15']").click()
time.sleep(2)
driver.quit()