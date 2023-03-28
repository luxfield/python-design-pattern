from CatalogAdapter import CatalogAdapter
from Screencast import Screencast


class ScreencastAdapter(CatalogAdapter):

    __screencast: Screencast

    def __init__(self, screencast: Screencast) -> None:
        self.__screencast = screencast

    def getCatalogTitle(self):
        return f'{self.__screencast.get_title()} by {self.__screencast.get_author()}'
