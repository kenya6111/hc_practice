from juice import Juice
from suica import Suica


class VendingMachine:
    def __init__(self, list_juice):
        initial_products = {Juice("ペプシ",150):5}
        self._list_drinks = initial_products
        self._list_drinks.update(list_juice)
        self._revenue = 0

    @property
    def list_drinks(self):
        return self.list_drinks
    @list_drinks.setter
    def list_drinks(self, list_drinks):
        if len(list_drinks) < 0:
            raise list_drinks
        self._list_drinks = list_drinks

    @property
    def revenue(self):
        return self.revenuş
    @revenue.setter
    def revenue(self, revenue):
        if len(revenue) < 0:
            raise revenue
        self._revenue = revenue

    def get_stock(self):
        return self._list_drinks

    def purchase_drink(self, name, buy_quantity, suica):
        d_num = self._list_drinks.get(name)
        new_d_num = d_num - buy_quantity
        if new_d_num < 0:
            return
        self._list_drinks.put(name, new_d_num)

        self.revenue += self.price * buy_quantity

        suica.deductBalance(self.price * buy_quantity)

    def get_current_revenue(self):
        return self.revenue
    # 自販機は購入可能なドリンクのリストを取得できる
    # 自販機に在庫を補充できる
    def add_stock(self, name, stock_num):
        d_num = self.list_drinks.get(name)
        new_d_num = d_num + stock_num
        self._list_drinks.put(name, new_d_num)



