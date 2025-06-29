#handling multiselect dropdowns
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
x = r"C:\chromedriver\chromedriver.exe"
service = Service(x)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://demo.mobiscroll.com/select/multiple-select")
dropdown = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[3]/div[2]/div[11]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/label[1]/span[2]/span[1]")
dd = Select(dropdown)
dd.select_by_index(2)
dd.select_by_index(3)
dd.deselect_all()
driver.quit()