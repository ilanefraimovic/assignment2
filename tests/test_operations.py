import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(3, 9) == 12

def test_subtraction():
    assert subtraction(9, 3) == 6

def test_multiplication():
    assert multiplication(3, 9) == 27

def test_division():
    assert division(9, 3) == 3

def test_division_zero():
    with pytest.raises(ZeroDivisionError):
        division(1,0)






