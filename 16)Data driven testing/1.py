##this is ddt(Data Driven Testing) module
# Import required libraries
import unittest  # Python's built-in testing framework
from ddt import ddt, data, unpack  # For data-driven testing

@ddt  # Decorator to enable DDT features
class TestLogin(unittest.TestCase):

    # Provide data as tuples of (username, password)
    @data(("admin", "admin123"), ("user1", "pass1"))
    @unpack  # Automatically unpack the tuple into individual arguments
    def test_login(self, username, password):
        # Just print the test data (simulate login)
        print("Trying login with:", username, password)

# Runs the test case
if __name__ == "__main__":
    unittest.main()
