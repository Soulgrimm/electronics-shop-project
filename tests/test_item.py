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


def test_name(test_class):
    item1 = test_class
    item1.name = 'Стол'
    assert item1.name == 'Стол'


def test_name2(test_class):
    item1 = test_class
    item1.name = 'Трансформатор'
    assert item1.name == 'Трансформа'


def test_string_to_number():
    assert Item.string_to_number('6.6666666')
    assert Item.string_to_number('6')
