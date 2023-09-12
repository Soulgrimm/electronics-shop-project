import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard_instance():
    return Keyboard('Light Project 88888', 1000, 6)


def test_expection(keyboard_instance):
    item = keyboard_instance

    assert str(item.language) == "EN"


def test_change_lang(keyboard_instance):
    item = keyboard_instance

    item.change_lang()
    assert str(item.language) == "RU"

    item.change_lang()
    assert str(item.language) == "EN"


def test_error(keyboard_instance):
    item = keyboard_instance

    with pytest.raises(AttributeError):
        item.language = 'CH'
