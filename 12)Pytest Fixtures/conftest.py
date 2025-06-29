#this conftest.py file is used to create a fixture which is a function that is used to setup and teardown the test cases
import pytest
@pytest.fixture(scope='session',autouse=True)
#if i use the autouse here then i need not to enter the setup in the methods of other files all the files will use this setup
#automatically without calling they inherit it
def setup():
    print("This is setup")
    yield
    print("This is teardown")
'''
if i use the scope as session then it will run only once in the whole session
'''
'''
in the 2_test.py file i have not used any of the setup in the method
but it has used the setup function which is defined in the conftest.py file
'''