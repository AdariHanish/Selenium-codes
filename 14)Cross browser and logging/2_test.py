#soft assertion using the pytest-check
import pytest_check as check
def test_multiple_soft_assertions():
    check.equal(2 + 2, 5, "Addition mismatch")               # ❌
    check.is_true(3 > 5, "3 is not greater than 5")          # ❌
    check.is_in("abc", "abcdef", "'abc' not found")          # ✅
    check.is_false(False, "Should be false")                 # ✅
    check.equal(len("hello"), 4, "Incorrect string length")  # ❌
    print("Test executed till end")
