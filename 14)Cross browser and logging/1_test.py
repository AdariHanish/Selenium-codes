#soft assertion
'''
these are the kind of assertions that are not fatal
if they fail the test will continue to run
at the end it will collect all the failed assertions and report them
'''
import softest
import pytest
class TestSoftAssertions(softest.TestCase):
    def test_multiple_conditions(self):
        self.soft_assert(self.assertEqual, 1, 2, "1 is not equal to 2")  # ❌
        self.soft_assert(self.assertTrue, False, "This should be true")  # ❌
        self.soft_assert(self.assertIn, "abc", "abcdef", "'abc' should be in 'abcdef'")  # ✅
        print("All assertions executed.")
        # Important: collect all failures
        self.assert_all()
a=TestSoftAssertions
a.test_multiple_conditions()