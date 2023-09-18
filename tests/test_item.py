"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone
from src.except_classes import InstantiateCSVError


@pytest.fixture
def test_class():
    return Item('Компьютер', 150000, 5)


@pytest.fixture
def phone_instance():
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


def test_issubclass(test_class, phone_instance):
    item1 = test_class
    item2 = phone_instance
    assert item1 + item2 == 7


def test_expection(test_class):
    item1 = test_class

    with pytest.raises(Exception):
        item1 + 10000


def test_instantiate_from_cs_1():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('item.csv')
        assert Item.instantiate_from_csv('item.csv') == 'Отсутствует файл item.csv'


def test_instantiate_from_cs_2():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('items2_invalid.csv')
        assert Item.instantiate_from_csv('items2_invalid.csv') == 'Файл items.csv поврежден'
