"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_class():
    return Item('Компьютер', 150000, 5)


def test_calculate_total_price(test_class):
    assert test_class.calculate_total_price() == 750000


def test_apply_discount(test_class):
    Item.pay_rate = 0.6
    test_class.apply_discount()
    assert test_class.price == 90000
