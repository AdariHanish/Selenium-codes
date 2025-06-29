import pytest
from base.base_test import initialize_driver
@pytest.fixture
def setup():
    driver = initialize_driver()
    driver.implicitly_wait(10) 
    yield driver
    driver.quit()