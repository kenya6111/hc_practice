from suica import Suica
from vending_machine import VendingMachine
from juice import Juice

if __name__== '__main__':
    mysuica = Suica()
    print(mysuica)
    print(mysuica.deposit)
    mysuica.deposit=10000
    print(mysuica.deposit)
    print(mysuica.charge(2))
    print(mysuica.deposit)
    print(mysuica.get_balance)
    mysuica.deduct_balance(100)
    print(mysuica.deposit)
    print("------------")


    monster = Juice("モンスター",230)
    irohasu = Juice("いろはす",120)
    print(monster.name)
    print(monster.price)
    list_juice = {monster:5, irohasu:5}

    vending_machine = VendingMachine(list_juice)
    print(vending_machine.list_drinks)

    vending_machine.purchase_drink("いろはす", 3, mysuica)
    for k,v in vending_machine.get_stock().items():
        print(k.name,v)
    print(vending_machine.get_current_revenue())
    vending_machine.add_stock("ペプシ", 15)
    for k,v in vending_machine.get_stock().items():
        print(k.name,v)



