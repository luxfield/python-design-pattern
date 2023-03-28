
from typing_extensions import Self
import copy

class Store:
    __name: str
    __city: str
    __country: str
    __category: str

    def __init__(self, name, city, country, category) -> None:
        self.__name = name
        self.__city = city
        self.__country = country
        self.__category = category

    def get_name(self):
        return self.__name

    def get_city(self):
        return self.__city

    def get_country(self):
        return self.__country

    def get_category(self):
        return self.__category

    def set_name(self, name):
        self.__name = name

        return self

    def set_city(self, city):
        self.__city = city

        return self

    def set_country(self, country):
        self.__country = country

        return self

    def set_category(self, category):
        self.__category = category

        return self

    def clone(self) -> Self:
        return copy.deepcopy(self)
