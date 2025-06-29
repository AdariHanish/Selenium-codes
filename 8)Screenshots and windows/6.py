#handling the frames
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
x = r"C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(service=Service(x), options=Options())
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
driver.maximize_window()
driver.switch_to.frame(1)
driver.find_element(By.XPATH, "//body/iframe[3]").click()
time.sleep(5)
print(driver.title)
driver.close()