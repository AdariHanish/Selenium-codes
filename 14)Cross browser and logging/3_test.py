#pytest-check example
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_homepage_ui():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    title = driver.title
    url = driver.current_url
    check.is_in("Example", title, "Title check failed")  # Soft check
    check.is_true("example" in url, "URL check failed")  # Soft check
    header = driver.find_element(By.TAG_NAME, "h1")
    check.is_true(header.is_displayed(), "Header not visible")  # Soft check
    driver.quit()