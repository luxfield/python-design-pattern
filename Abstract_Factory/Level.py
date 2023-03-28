from abc import ABC, abstractmethod


class Level(ABC):

    @abstractmethod
    def start(self):
        pass


class LevelEasy(Level):
    def start(self):
        print('Level Easy')


class LevelMedium(Level):
    def start(self):
        print('Level Medium')


class LevelHard(Level):
    def start(self):
        print('Level Hard')
