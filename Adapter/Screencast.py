class Screencast:
    __title: str
    __author: str
    __duration: int

    def __init__(self, title, author, duration) -> None:
        self.__author = author
        self.__duration = duration
        self.__title = title

    def get_author(self):
        return self.__author

    def get_duration(self):
        return self.__duration

    def get_title(self):
        return self.__title

    def set_author(self, author):
        self.__author = author

    def set_duration(self, duration):
        self.__duration = duration

    def set_title(self, title):
        self.__title = title
