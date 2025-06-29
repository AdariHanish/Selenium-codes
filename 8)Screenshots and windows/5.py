#handling multiple windows advanced
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
r = r'c:\chromedriver\chromedriver.exe'
service = Service(r)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get("http://amazon.in")
# gives the unique id of the current window
parent = driver.current_window_handle
driver.maximize_window()
print(parent)
driver.implicitly_wait(20)
x = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
x.send_keys("samsung s24")
p = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
p.click()
driver.find_element(By.XPATH, "//img[@alt='Samsung Galaxy S24 5G AI Smartphone (Onyx Black, 8GB, 256GB Storage)']").click()
all = driver.window_handles
for window in all:
    if window != parent:
        driver.switch_to.window(window)
        print(driver.title)
        driver.find_element(By.XPATH, "//div[@id='averageCustomerReviews_feature_div']//span[@id='acrCustomerReviewText']").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "See all photos").click()
        time.sleep(2)
        print(driver.title)
        driver.close()
driver.switch_to.window(parent)
print(driver.title)
time.sleep(20)