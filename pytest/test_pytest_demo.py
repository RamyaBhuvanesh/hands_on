'''
1.ordering
2.html report
'''

import pytest

@pytest.fixture()
def setUP():
    print("\n this is SetUP at start\n")
    yield
    print("\n this is teardown at start\n")

@pytest.mark.run(order=1)
def test_methodA(setUP):
    print("\n this is method A \n")

def test_methodB(setUP):
    print("\n this is method B \n")

def test_methodC(setUP):
    print("\n this is method C \n")



