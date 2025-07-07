#grouping file continution
import pytest
def testlogin():  #methods should always start with test and followed by the method name if not methods wont accept
    print("this is login test")
def testlogout():
    print("this is logout test")
@pytest.mark.anything #this is a decorator which executes the test case if it is marked with the name(anything)
def testhome():
    print("this is home test")
@pytest.mark.skip #this is a decorator which skips the test case if it is marked with the name(skip) and the testcal wont execute
def testcal():
    assert 10+2 == 12