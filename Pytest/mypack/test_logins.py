import pytest
from _pytest import assertion

def test_LoginByEmail(setup):
    print("This is login by email test")
    assert True==True

def test_LoginByFacebook(setup):
    print("This is login by Facebook test")
    assert True==True
def test_LoginByPhone(setup ):
    print("This is login by Phone test")
    assert True==True


# assert is used to verify whether a condition is true.
# Assertions  It is nothing but a vadilation point.If Assertion passes login will pass ,if fail asseration will fail
# In pytest if we want to add any assertion we will use onekeyword call "assert"