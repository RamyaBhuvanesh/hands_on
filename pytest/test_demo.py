import pytest
@pytest.fixture
def setUP():
    print("\n this is a setup line\n")
    yield
    print("\nthis is teared down step \n")

def test_funa(setUP):
    print("the value is a")

def test_funb(setUP):
    print("the value is b")