#grouping test by using the .mark decorator
#this file is grouped with the 4_test.py file
import pytest
@pytest.mark.anything
def testcal():
    assert 10+2 == 12
#to run this type the command (pytest -m anything) in the terminal to run all the methods that have the mark (anyting)