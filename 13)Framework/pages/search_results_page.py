from selenium.webdriver.common.by import By
from base.base_page import BasePage

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Updated locator for iPhone 15 search result
    first_result_title = (By.CSS_SELECTOR, 'div.KzDlHZ')  # This is the current class for product title

    def get_first_product_title(self):
        return self.get_element_text(self.first_result_title)
