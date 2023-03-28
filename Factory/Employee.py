class Employee:
    __name: str
    __title: str
    __salary: str

    def __init__(self, name: str, title: str, salary: str) -> None:
        self.__name = name
        self.__title = title
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_title(self):
        return self.__title

    def get_salary(self):
        return self.__salary

    def get_detail(self) -> None:
        print(f'Nama : {self.__name}\nJabatan : {self.__title}\nGaji: {self.__salary}')
