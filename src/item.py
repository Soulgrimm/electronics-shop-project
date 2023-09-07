import csv
import os.path

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise Exception

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, string_name):
        if len(string_name) > 10:
            self.__name = string_name[:10]
        self.__name = string_name

    @classmethod
    def instantiate_from_csv(cls, items):
        path_to_file = os.path.join(os.path.dirname(__file__), items)
        with open(path_to_file, newline='', encoding='windows-1251') as csvf:
            reader = csv.DictReader(csvf)

            for row in reader:
                cls(row['name'], int(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(str_):
        return int(float(str_))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
