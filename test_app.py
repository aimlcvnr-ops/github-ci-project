import pytest
from app import add,sub,multi,divi

def test_add():
    assert add(10,5)==15

def test_sub():
    assert sub(10,5)==5

def test_multi():
    assert multi(10,5)==50

def test_divi():
    assert divi(10,5)==2

def test_divi_zero():
    with pytest.raises(ValueError):
        divi(10,0)