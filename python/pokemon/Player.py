from abc import ABC, abstractmethod
from NameService import NameService
class Player(NameService,ABC):


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
    def age(self):
        # return self.__name
        pass
    @property
    @abstractmethod
    def name(self):
        # return self.__name
        pass
    @abstractmethod
    def walk(self):
        pass
    # @abstractmethod
    # def attack(self):
    #     pass

    # @abstractmethod
    # def change__name(self):
    #     pass