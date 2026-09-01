

import pytest
@pytest.fixture
def setup():
    print("Open Browser")
    return "Chrome Opened"

def test_one(setup):
    print("Test One is Passed")
    print(setup)
def test_two(setup):
    print("Test Two Passed")
def test_three(setup):
    print("Test Three is Passed")
    print(setup)

"""
Fixtures not only doing some tasks or not only printing the output ,it is able to return the value
we can get the return value in test function

. A fixture can return a value (or yield a value), 
and Pytest automatically passes that value to the test function.

"""