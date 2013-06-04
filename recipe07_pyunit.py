__author__ = 'jinpeng'

from recipe07 import *
from recipe07_legacy import *

import unittest

if __name__ == "__main__":
    tester = RomanNumeralTester()
    suite = unittest.TestSuite()
    for test in [tester.simple_test, tester.combo_test1, tester.combo_test2, tester.other_test]:
        testcase = unittest.FunctionTestCase(test)
        suite.addTest(testcase)

    unittest.TextTestRunner(verbosity=2).run(suite)