class Book:
    __title: str
    __author: str

    def __init__(self, title, author) -> None:
        self.__author = author
        self.__title = title

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author
