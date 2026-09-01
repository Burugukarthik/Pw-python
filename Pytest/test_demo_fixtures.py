# Fixtures:Re-usable function
# we can re use it multiple times
# Fixtures help avoid writing the same code repeatedly in multiple test cases.
'''
import pytest

# Annotation we have to had because to use that function reusable
@pytest.fixture
def setup():
    print("setup browser...")

# I want to execute this setup function for every Test function
#      before excuting the test_three i want to run setup()

 # without passing parameter (setup) it wont execute setup function
def test_one(setup):
    print("this is my one")

def test_two(setup):
    print("this is my two")

def test_three(setup):
    print("this is my three")
'''
import pytest
@pytest.fixture
def setup():
    print("setup login page...")
def test_click(setup):
    print("this is my click")

def test_button():
    print("this is my button")
def test_text(setup):
    print("this is my text")
"""
Function → Every Test
Class → Every Class
Module → Every File
Session → Entire Framework Run

Function = One Browser Per Test

Class = One Browser Per Class

Module = One Browser Per File

Session = One Resource For Entire Framework
    """

