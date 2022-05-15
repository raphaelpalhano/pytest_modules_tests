import pytest
from project.calc.calcutation import Calculation


# Fixtures
@pytest.fixture
def calculation():
    return Calculation()


# Parameter what was used:
listValues = [
    (1,2,3,4,10),
    (2,4,8,16,30),
    (4,8,16,32,60),
    (8,16,32,64,120),
    (16,32,64,128,240),
    ]

# decorator for select quantity element into tuple
@pytest.mark.parametrize('a, b, c, d, e', listValues)
def test_sum_ten_numbers(a, b, c, d, e, calculation):
    calculation.addValues(a,b,c,d)
    assert calculation.sumValues() == e


