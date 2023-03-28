from abc import ABC, abstractmethod
from Level import LevelEasy, LevelMedium, LevelHard, Level
from Arena import ArenaEasy, ArenaMedium, ArenaHard, Arena
from Enemy import EnemyEasy, EnemyMedium, EnemyHard, Enemy


class GameFactory(ABC):

    @abstractmethod
    def create_level(self):
        return Level

    @abstractmethod
    def create_arena(self):
        return Arena

    @abstractmethod
    def create_enemy(self):
        return Enemy


class GameFactoryEasy(GameFactory):
    def create_level(self):
        return LevelEasy()

    def create_arena(self):
        return ArenaEasy()

    def create_enemy(self):
        return EnemyEasy()


class GameFactoryMedium(GameFactory):
    def create_level(self):
        return LevelMedium()

    def create_arena(self):
        return ArenaMedium()

    def create_enemy(self):
        return EnemyMedium()


class GameFactoryHard(GameFactory):
    def create_level(self):
        return LevelHard()

    def create_arena(self):
        return ArenaHard()

    def create_enemy(self):
        return EnemyHard()
