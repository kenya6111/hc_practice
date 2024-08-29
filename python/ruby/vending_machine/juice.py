
class Juice:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, val):
        if len(val) < 0:
            raise ValueError("値が不正です")
        self._name = val

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, val):
        if len(val) < 0:
            raise ValueError("値が不正です")
        self._price = val