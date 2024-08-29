from suica import Suica
from vending_machine import VendingMachine
from juice import Juice

if __name__== '__main__':
    mysuica = Suica()
    print(mysuica)
    print(mysuica.deposit)


    monster = Juice("モンスター",230)
    irohasu = Juice("いろはす",120)
    list_juice = {monster:5, irohasu:5}

    Vending_machine = VendingMachine(list_juice)

