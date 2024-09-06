from abc import ABC, abstractmethod
from NameService import NameService
class Pokemon(NameService,ABC):


    @abstractmethod
    def __init__(ABC):
        pass

    @property
    @abstractmethod
    def name(self):
        # return self.__name
        pass

    @property
    @abstractmethod
    def type1(self):
        # return self.__type1
        pass

    @property
    @abstractmethod
    def type2(self):
        # return self.__type2
        pass

    @property
    @abstractmethod
    def hp(self):
        # return self.__hp
        pass

    @abstractmethod
    def attack(self):
        pass

    # @abstractmethod
    # def change__name(self):
    #     pass