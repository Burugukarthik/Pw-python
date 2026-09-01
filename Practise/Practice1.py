import pytest
@pytest.fixture
def setup():
    print("Opeing the Chrome Browser")
    yield
    print("Closing the Chrome Browser")

def test_one(setup):
    print("Testing the web Browser")

def test_two(setup):
    print("Testing the Login page")

def test_three(setup):
    print("Testing the whether page is re-directing to the Web page")