import pytest
def testlogin():  #methods should always start with test and followed by the method name if not methods wont accept
    print("login test")
def testlogout():
    print("logout test")
def testhome():
    print("home test")
@pytest.mark.xfail #this will mark the test as xfail and will not fail even if the test fails (it wont show as the error)
def testcal():
    assert 2+3 == 6