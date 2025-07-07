import pytest
@pytest.fixture(autouse=True)#if autouse=True then we dont need to pass the fixture in the test method 
def setup():
    print("This is setup method")
    yield
    print("This is teardown method")

def testlogin():
    print("This is login method")

def testlogout():
    print("This is logout method")