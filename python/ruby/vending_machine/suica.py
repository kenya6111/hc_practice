class Suica:

    def __init__(self):
        self.__deposit = 500

    @property
    def deposit(self):
        return self.__deposit
    @deposit.setter
    def deposit(self, deposit):
        if deposit < 0:
            raise ValueError("")
        self.__deposit = deposit
        return True

    def charge (self , money):
        if money < 100:
            raise ValueError("チャージ金額は100円~になります。")
        self.__deposit+= money
        return True #正常に処理が終了

    def get_balance(self):
        return self.__deposit

    def deduct_balance(self, purchase_money):
        if self.__deposit < purchase_money:
            raise ValueError()
        self.__deposit -= purchase_money
        return True #正常に処理が終了