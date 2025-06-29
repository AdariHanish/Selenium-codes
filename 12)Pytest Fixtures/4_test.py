#more parameters in fixture
import pytest
@pytest.mark.parametrize("a,b,final",[(2,6,8),(3,9,12),(4,12,16)])
def testadd(a,b,final):
    print(f"{a}+{b}={final}")
    assert a+b==final