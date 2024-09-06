
from Pikachu import Pikachu
from zeni import Zeni



if __name__ == '__main__':

    # pikachu = Pokemon("ピカチュウ","でんき"," ",100)
    # print(pikachu.name)
    # print(pikachu.type1)
    # print(pikachu.type2)
    # print(pikachu.hp)

    # 抽象化したのでインスタンンス化はできない
    # poke = Pokemon()

    pikachu = Pikachu("ピカチュウ","でんき"," ",100)
    print(pikachu.name)
    print(pikachu.type1)
    print(pikachu.type2)
    print(pikachu.hp)
    pikachu.attack()

    zeni = Zeni("ゼニガメ","水"," ",100)
    print(zeni.name)
    print(zeni.type1)
    print(zeni.type2)
    print(zeni.hp)
    zeni.attack()
    zeni.change__name("ゼニゼニ〜")
    print(zeni.name)
    zeni.nam = "zzzzz"
    print(zeni.name)
    