import unittest
import glob
import sys
import os

def create_test_suite():
	print __file__
	test_file_strings = glob.glob('*_test.py')
	module_strings = [str[0:len(str)-3] for str in test_file_strings]
	suites = [unittest.defaultTestLoader.loadTestsFromName(name) for name in module_strings]
	testSuite = unittest.TestSuite(suites)
	return testSuite

d = os.path.dirname(__file__)
if (d): os.chdir(d)
sys.path.insert(0, "..")

testSuite = create_test_suite()
text_runner = unittest.TextTestRunner().run(testSuite)