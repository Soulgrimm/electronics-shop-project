import pytest
from src.phone import Phone


@pytest.fixture
def test_class1():
    return Phone("Xiaomi", 1500, 2, 6)


def test_expection(test_class1):
    item2 = test_class1

    with pytest.raises(Exception):
        item2 + 15000
