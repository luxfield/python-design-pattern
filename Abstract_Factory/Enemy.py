from abc import ABC, abstractmethod


class Enemy(ABC):

    @abstractmethod
    def start(self):
        pass


class EnemyEasy(Enemy):
    def start(self):
        print('Enemy Easy')


class EnemyMedium(Enemy):
    def start(self):
        print('Enemy Medium')


class EnemyHard(Enemy):
    def start(self):
        print('Enemy Hard')
