from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=10):
    # Utility to wait for element presence in the DOM
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
