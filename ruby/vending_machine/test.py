class Suica:

    def __init__(self):
        self.deposit = 500

    def charge (self , money):
        if money < 100:
            print("例外発生")
            return

        self.deposit+= money
    def get_balance(self):
        return self.deposit
    def deductBalance(self, purchace_money):
        self.deposit -= purchace_money

class Juice:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, name):
        if len(name) < 0:
            raise ValueError("名前が不正です")
        self.name = name

class VendingMachine:

    def __init__(self, list_juice):
        self.drinks = list_juice
        self.revenue = 0

    def get_stock(self):
        return self.drinks_num

    def purchase_drink(self, buy_quantity, balance, suica):
        if self.drinks_num < buy_quantity:
            return
        if self.price * buy_quantity > balance:
            return

        self.drinks_num -= buy_quantity
        self.revenue += self.price * buy_quantity
        suica.deductBalance(self.price * buy_quantity)

    def get_current_revenue(self):
        return self.revenue



if __name__== '__main__':
    print("aa")