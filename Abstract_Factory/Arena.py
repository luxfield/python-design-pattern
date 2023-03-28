from abc import ABC, abstractmethod


class Arena(ABC):

    @abstractmethod
    def start(self):
        pass


class ArenaEasy(Arena):
    def start(self):
        print('Arena Easy')


class ArenaMedium(Arena):
    def start(self):
        print('Arena Medium')


class ArenaHard(Arena):
    def start(self):
        print('Arena Hard')
