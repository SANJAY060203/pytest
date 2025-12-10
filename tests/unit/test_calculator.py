import pytest
from src.calculator import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

@pytest.mark.parametrize("a,b,r", [(10,5,5), (20,10,10)])
def test_sub(a, b, r):
    assert sub(a,b) == r

def test_div_zero():
    with pytest.raises(ValueError):
        div(1,0)
