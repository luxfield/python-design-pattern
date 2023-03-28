from CatalogAdapter import CatalogAdapter
from Book import Book


class BookAdapter(CatalogAdapter):

    __book: Book

    def __init__(self, book: Book) -> None:
        self.__book = Book

    def getCatalogTitle(self):
        return f'{self.__book.get_title()} by {self.__book.get_author()}'
