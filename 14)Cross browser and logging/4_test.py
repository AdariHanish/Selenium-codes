#running test case on multiple browsers
import pytest
from selenium import webdriver

# Parametrize the test to run with different browsers
@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_open_google(browser):
    driver = None

    # Setup browser driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Unsupported browser: {browser}")

    # Maximize window and run test
    driver.maximize_window()
    driver.get("https://www.google.com")
    
    assert "Google" in driver.title

    driver.quit()