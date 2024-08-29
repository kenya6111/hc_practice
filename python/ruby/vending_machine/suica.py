class Suica:

    def __init__(self):
        self.__deposit = 500

    @property
    def deposit(self):
        return self.__deposit
    @deposit.setter
    def deposit(self, deposit):
        self.__deposit = deposit

    def charge (self , money):
        if money < 100:
            return money
        self.__deposit+= money

    def get_balance(self):
        return self.deposit

    def deductBalance(self, purchase_money):
        if self.__deposit < purchase_money:
            return purchase_money
        self.__deposit -= purchase_money