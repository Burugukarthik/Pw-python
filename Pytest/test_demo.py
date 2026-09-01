# we have to import pytest module before starting any pytest cases

# this functions are pytest test functions we dont call again

# By default pytest wont display outputs it will just written pass or fail
'''
pytest -v
 -v stands for verbose mode. It displays detailed test execution information,
including test names and their status.
'''
"""
pytest Pytest/test_demo.py
pytest Pytest/test_demo.py -s
pytest Pytest/test_demo.py -s -v 
pytest Pytest/test_demo.py::test_one --->single function execution


"""

import pytest
'''
def test_one():
    print("this is my one")

def test_two():
    print("this is my two")

def test_three():
    print("this is my three")
'''

class TestClass:
    def test_one(self):
        print("this is my test one")
    def test_two(self):
        print("this is my test two")
    def test_three(self):
        print("this is my test three")