import pytest
from src.phone import Phone


@pytest.fixture
def phone_instance():
    return Phone("Xiaomi", 1500, 2, 6)


def test_expection(phone_instance):
    item2 = phone_instance

    with pytest.raises(Exception):
        item2 + 15000
