from abc import ABC, abstractmethod


class CatalogAdapter(ABC):
    @abstractmethod
    def getCatalogTitle(self):
        pass