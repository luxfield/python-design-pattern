from GameFactory import GameFactory
class Game:
    __level: GameFactory
    __arena: GameFactory
    __enemy: GameFactory

    def __init__(self, game_factory: GameFactory) -> None:
        self.__level = game_factory.create_level()
        self.__arena = game_factory.create_arena()
        self.__enemy = game_factory.create_enemy()

    def start(self):
        self.__level.start()
        self.__arena.start()
        self.__enemy.start()