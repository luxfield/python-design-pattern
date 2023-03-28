from Game import Game
from GameFactory import GameFactoryEasy, GameFactoryMedium, GameFactoryHard


game1 = Game(GameFactoryMedium())
game1.start()