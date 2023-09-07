"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_class():
    return Item('Компьютер', 150000, 5)


@pytest.fixture
def test_class1():
    return Phone("Xiaomi", 1500, 2, 6)


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


def test_repr(test_class):
    item1 = test_class
    assert repr(item1) == "Item('Компьютер', 150000, 5)"


def test_str(test_class):
    item1 = test_class
    assert str(item1) == 'Компьютер'


def test_issubclass(test_class, test_class1):
    item1 = test_class
    item2 = test_class1
    assert item1 + item2 == 7


def test_expection(test_class, test_class1):
    item1 = test_class

    with pytest.raises(Exception):
        item1 + 10000
