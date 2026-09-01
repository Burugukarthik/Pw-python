
import pytest
@pytest.fixture
def setup():
    print("Open Browser")
    yield
    print("Close Browser")

def test_one(setup):
    print("Test One is Passed")

def test_two(setup):
    print("Test Two Passed")
def test_three(setup):
    print("Test Three is Passed")

"""
In Pytest fixtures, yield divides the fixture into two parts:

Code before yield → Setup
Code after yield → Teardown

The setup fixture runs before every test because the default fixture scope is function. 
The code before yield acts as setup, the test executes when control reaches yield, 
and the code after yield acts as teardown. 
Therefore, for each test, the browser is opened before execution and closed after execution.
"""
