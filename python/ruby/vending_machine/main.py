from suica import Suica
from vending_machine import VendingMachine
from juice import Juice

if __name__== '__main__':
    try:
        print("-----juice.pyの動作確認-----")
        mysuica = Suica()
        print(mysuica)
        print(mysuica.deposit)
        mysuica.deposit=10000
        print(mysuica.deposit)
        print(mysuica.deposit)
        print(mysuica.get_balance)
        mysuica.deduct_balance(100)
        print(mysuica.deposit)


        print("-----suica.pyの動作確認-----")
        monster = Juice("モンスター",230)
        irohasu = Juice("いろはす",120)
        monster.price=-100
        print(monster.name)
        print(monster.price)
        list_juice = {monster:5, irohasu:5}


        print("-----vending_machine.pyの動作確認-----")
        vending_machine = VendingMachine(list_juice)
        print(vending_machine.list_drinks)
        print(f"売上 : {vending_machine.get_current_revenue()}円")

        vending_machine.purchase_drink("いろはす", 3, mysuica)
        for k,v in vending_machine.get_stock().items():
            print(f"商品名:{k.name}, 値段:{k.price}円, 本数:{v}本")
        print(f"売上 : {vending_machine.get_current_revenue()}円")
        vending_machine.add_stock("ペプシ", 15)
        for k,v in vending_machine.get_stock().items():
            print(f"商品名:{k.name}, 値段:{k.price}円, 本数:{v}本")

    except ValueError as e:
        print(f"エラーが発生しました: {e}")




