#parameterising the pytest fixture
import pytest
@pytest.fixture(params=["a","b"])
def demo(request):
    print(request.param)
def testlogin(demo):
    print("login")
    return demo
'''
o/p:-
3_test.py::testlogin[a] This is setup
a
login
PASSED
3_test.py::testlogin[b] b
login
PASSEDThis is teardown
why this is happening because we are using the same fixture in two different test cases
and this is setup is printing before the test cases and teardown is printing after the test cases this is beacuse
we have declared the fixture scope is session means until entire session executes it wont print teardown
'''