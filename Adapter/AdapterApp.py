from Book import Book
from Screencast import Screencast
from BookAdapter import BookAdapter
from ScreencastAdapter import ScreencastAdapter

from CatalogAdapter import CatalogAdapter
class AdapterApp:
    daftar:CatalogAdapter = []

    daftar.append(BookAdapter(Book("Pemrograman Java","Eko")))
    daftar.append(BookAdapter(Book("Pemrograman PHP","Kurniawan")))
    daftar.append(BookAdapter(Book("Pemrograman Python","Khannedy")))

    daftar.append(ScreencastAdapter(Screencast("Web Laravel","Joko",1000)))
    daftar.append(ScreencastAdapter(Screencast("Web Rails","Budi",1000)))
    daftar.append(ScreencastAdapter(Screencast("Flask Web","Ardi",1000)))

    print(daftar.__dir__())
