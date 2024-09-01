from juice import Juice
from suica import Suica


class VendingMachine:
    def __init__(self, list_juice):
        initial_products = {Juice("ペプシ",150):5}
        self.__list_drinks = initial_products
        self.__list_drinks.update(list_juice)
        self.__revenue = 0

    @property
    def list_drinks(self):
        return self.__list_drinks
    @list_drinks.setter
    def list_drinks(self, list_drinks):
        if not isinstance(list_drinks, dict):
            raise ValueError("データ型が辞書型でありません")
        self.__list_drinks = list_drinks

    @property
    def revenue(self):
        return self.__revenue
    @revenue.setter
    def revenue(self, revenue):
        if revenue < 0:
            raise ValueError("売上金額は0円~を設定してください")
        self.__revenue += revenue

    def get_stock(self):
        return self.__list_drinks

    def purchase_drink(self, name, buy_quantity, suica):
        target_juice = None
        for key in self.__list_drinks.keys():
            if key.name == name:
                target_juice = key
                break
        if target_juice is None:
            raise ValueError("指定の飲み物はありません")
        stock = self.list_drinks[target_juice]
        if stock < buy_quantity:
            raise ValueError("在庫が不足しています")
        if suica.get_balance() < target_juice.price * buy_quantity:
            raise ValueError("残高が不足しています")
        self.__list_drinks[target_juice] -= buy_quantity
        self.__revenue += target_juice.price * buy_quantity
        suica.deduct_balance(target_juice.price * buy_quantity)
        return True #　正常に処理が終了

    def get_current_revenue(self):
        return self.revenue

    def add_stock(self, name, stock_num):
        target_juice = None
        for key in self.__list_drinks.keys():
            if key.name == name:
                target_juice = key
                break
        if target_juice is None:
            raise ValueError("指定の飲み物はありません")
        self.__list_drinks[target_juice] += stock_num
        return True #　正常に処理が終了



