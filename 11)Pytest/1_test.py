#sample or test code to run the pytest
'''
the file name should start with _test and the name of the file and then the .py extension
or it can also be named as the filename _test.py
if the _test is not there in the starting or ending of the file then 
it wont be or read as a test file and wont run in the pytest
'''
def testlogin():  #methods should always start with test and followed by the method name if not methods wont accept
    print("login test")
def testlogout():
    print("logout test")
def testhome():
    print("home test")
def testcal():
    assert 2+3 == 5
    