#takes the screen shot of the page when the failure ocurs and saves in the same directory
import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Launch Chrome browser
    yield driver
    driver.quit()  # Close after test

def test_title(setup):
    driver = setup
    driver.get("https://www.google.com")
    assert driver.title == "Wrong Title"  # This will fail

# Hook to capture screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        driver = item.funcargs['setup']
        driver.save_screenshot("failed_test.png")  # Save screenshot