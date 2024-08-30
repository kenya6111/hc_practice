
class Juice:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, val):
        if val < 0:
            return None
        self.__name = val

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, val):
        if val < 0:
            return None
        self.__price = val