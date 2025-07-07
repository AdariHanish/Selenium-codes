from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout  # default timeout for explicit/fluent waits
        self.driver.implicitly_wait(10)  # ✅ Implicit wait

    # ✅ Explicit Wait for Click
    def click(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            print(f"[INFO] Clicked on element {locator}")
        except TimeoutException:
            print(f"[ERROR] Element not clickable: {locator}")
            self.driver.save_screenshot("screenshots/click_error.png")
            raise

    # ✅ Explicit Wait for Typing Text
    def send_keys(self, locator, text):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.send_keys(text)
            print(f"[INFO] Sent keys to element {locator}")
        except TimeoutException:
            print(f"[ERROR] Timeout when sending keys to {locator}")
            self.driver.save_screenshot("screenshots/send_keys_timeout.png")
            raise

    # ✅ Explicit Wait for Text Retrieval
    def get_element_text(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            print(f"[INFO] Found element: {locator}")
            return element.text
        except TimeoutException:
            print(f"[ERROR] Element text not found: {locator}")
            self.driver.save_screenshot(f"screenshots/error_{locator[1].replace(' ', '_')}.png")
            raise

    # ✅ Explicit Wait to Check Visibility
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            print(f"[WARN] Element not visible: {locator}")
            return False

    # ✅ Explicit Wait to Clear & Enter Text
    def enter_text(self, locator, text):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
            print(f"[INFO] Entered text '{text}' in element {locator}")
        except TimeoutException:
            print(f"[ERROR] Unable to enter text. Element not visible: {locator}")
            self.driver.save_screenshot("screenshots/enter_text_error.png")
            raise

    # ✅ Optional Fluent Wait (Advanced)
    def wait_for_element_fluent(self, locator, timeout=15, poll_frequency=1.0):
        try:
            wait = WebDriverWait(
                self.driver,
                timeout=timeout,
                poll_frequency=poll_frequency,
                ignored_exceptions=[NoSuchElementException, ElementClickInterceptedException]
            )
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"[ERROR] Fluent wait failed for element: {locator}")
            self.driver.save_screenshot("screenshots/fluent_wait_timeout.png")
            raise
