import pytest
from project.calc.calcutation import Calculation

def test_sum_ten_numbers():
    calculation = Calculation(10,20,30,40,50,60,70,80,90,100)
    assert calculation.sumValues() == 550

def test_subtraction_five_numbers():
    calculation = Calculation(5,10,15,20,25)
    assert calculation.subtraction() == -65

def test_fail_sum():
    calculation = Calculation(10,10)
    assert calculation.sumValues() == 20

def test_exception():
    calculation = Calculation(10,0)
    assert 'division by zero' in str(calculation.division())


