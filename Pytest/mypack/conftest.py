import pytest
@pytest.fixture()
def setup():
    print("Setup Environment")
    yield
    print("Tear Down Environment......////")

    """
    What is conftest.py in Pytest?
--->conftest.py is a special Pytest file used to store shared fixtures, hooks, and configuration settings. 
    Fixtures defined in conftest.p y are automatically available to all test files in that directory and its 
    subdirectories without needing explicit imports.
    """
