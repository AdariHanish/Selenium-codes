import configparser
from selenium import webdriver

def initialize_driver():
    config = configparser.ConfigParser()
    config.read('configfiles/config.ini')

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(config['DEFAULT']['base_url'])
    return driver
