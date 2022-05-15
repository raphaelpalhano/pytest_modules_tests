import pytest
from project.calc.calcutation import Calculation


# Fixture: inicia a instância da classe para evitar a repetição do objeto
@pytest.fixture
def calculation():
    return Calculation()


def test_sum_ten_numbers(calculation):
    calculation.addValues(10,20,30,40,50,60,70,80,90,100)
    assert calculation.sumValues() == 550

def test_subtraction_five_numbers(calculation):
    calculation.addValues(5,10,15,20,25)
    assert calculation.subtraction() == -65

def test_fail_sum(calculation):
    calculation.addValues(10,10)
    assert calculation.sumValues() == 20

def test_exception(calculation):
    calculation.addValues(10,0)
    assert 'division by zero' in str(calculation.division())


