from Pokemon import Pokemon

class Pikachu(Pokemon):
    def __init__(self,name, type1, type2, hp):
        self.___name = name
        self.___type1 = type1
        self.___type2 = type2
        self.___hp = hp
    @property
    def name(self):
        return self.___name
    @name.setter
    def name(self, name):
        self.___name = name

    @property
    def type1(self):
        return self.___type1
    @type1.setter
    def type1(self, type1):
        self.___type1 = type1

    @property
    def type2(self):
        return self.___type2
    @type2.setter
    def type2(self, type2):
        self.___type2 = type2

    @property
    def hp(self):
        return self.___hp

    @hp.setter
    def hp(self, hp):
        self.___hp = hp

    def attack(self):
        print(f"{self.___name}の10マンボルト！")

    def change__name(self, new__name):
        if new__name =='うんこ':
            print("不適切な名前です")
            return
        self.___name = new__name