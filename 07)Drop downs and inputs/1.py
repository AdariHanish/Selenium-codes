#handling drop down
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
x = r"c:\chromedriver\chromedriver.exe"
service = Service(x)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://www.salesforce.com/in/form/sem/salesforce-crm/?d=7013y0000026rGRAAY&nc=7013y000000a9thAAA&utm_source=google&utm_medium=paid_search&utm_campaign=apac_in_alllobcon&utm_content=apac-en-multi-product-text_salesforce-crm_7013y0000026rGRAAY&utm_term=salesforce&ef_id=CjwKCAjwtdi_BhACEiwA97y8BHNZduGTFthK2CTQGsOOYYvBdsJjlnSDXWcBC8-YbzrEn2p-YJTZIBoCoxgQAvD_BwE:G:s&s_kwcid=AL!4720!3!720291834476!e!!g!!sales%20force&&ev_sid=3&ev_ln=sales%20force&ev_lx=kwd-18613152&ev_crx=720291834476&ev_mt=e&ev_n=g&ev_ltx=&ev_pl=&ev_pos=&ev_dvc=c&ev_dvm=&ev_phy=9197649&ev_loc=&ev_cx=16895847353&ev_ax=170243680499&ev_efid=CjwKCAjwtdi_BhACEiwA97y8BHNZduGTFthK2CTQGsOOYYvBdsJjlnSDXWcBC8-YbzrEn2p-YJTZIBoCoxgQAvD_BwE:G:s&url=!https://clickserve.dartsearch.net/link/click?lid=43700081024291499&ds_s_kwgid=58700008806451955&gad_source=1&gclid=CjwKCAjwtdi_BhACEiwA97y8BHNZduGTFthK2CTQGsOOYYvBdsJjlnSDXWcBC8-YbzrEn2p-YJTZIBoCoxgQAvD_BwE&gclsrc=aw.ds%22")
dropdown = (driver.find_element(By.NAME, "UserTitle"))
dd = Select(dropdown)
dd.select_by_index(3)
time.sleep(3)
dd.select_by_value("Sales_Manager_AP")
time.sleep(5)
print(driver.title)
driver.quit()