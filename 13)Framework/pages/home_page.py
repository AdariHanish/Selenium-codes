from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    search_box = (By.NAME, "q")
    search_button = (By.CSS_SELECTOR, "button[type='submit']")
    close_login_popup_btn = (By.XPATH, "//button[text()='✕']")  # Replace with actual close button locator

    def close_login_popup(self):
        from time import sleep
        print("[INFO] Checking if login popup is visible...")
        try:
            if self.is_element_visible(self.close_login_popup_btn):
                print("[INFO] Login popup found. Closing it...")
                sleep(1)  # Or replace with WebDriverWait if you want better sync
                self.click(self.close_login_popup_btn)
                print("[INFO] Login popup closed.")
            else:
                print("[INFO] Login popup not found.")
        except Exception as e:
            print(f"[WARNING] Failed to close popup: {e}")

    def search_item(self, item_name):
        print(f"[INFO] Searching for item: {item_name}")
        self.send_keys(self.search_box, item_name)
        self.click(self.search_button)
        
        # Optional: wait for search bar to be visible again if the page reloads
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.NAME, "q"))
        ).send_keys(item_name)

