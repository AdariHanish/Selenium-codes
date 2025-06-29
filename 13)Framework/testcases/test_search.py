import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import configparser
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

def test_search_functionality(setup):
    # Read configuration values
    config = configparser.ConfigParser()
    config.read("configfiles/config.ini")

    driver = setup  # Get the WebDriver from fixture

    # Initialize page objects
    home = HomePage(driver)
    home.close_login_popup()
    home.search_item(config["DEFAULT"]["search_item"])

    result_page = SearchResultsPage(driver)
    product_name = result_page.get_first_product_title()

    # Print product title for debugging
    print(f"First product title: {product_name}")

    # Assertion to verify search functionality
    assert config["DEFAULT"]["search_item"].lower() in product_name.lower()
