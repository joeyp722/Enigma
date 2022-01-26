# Main test script that performs unittest on all the test files.
import unittest

# Define which test scripts are executed.
def load_tests(loader, tests, pattern):

    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('test_files', pattern='test*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

# Execute the tests defined above.
if __name__ == '__main__':
    unittest.main()
