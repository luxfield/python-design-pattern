from Customer import Customer


class CustomerBuilder:
    __lastname: str = ""

    def set_id(self, id: str):
        self.__id = id
        return self

    def set_firstname(self, firstname: str):
        self.__firstname = firstname
        return self

    def set_lastname(self, lastname: str):
        self.__lastname = lastname
        return self

    def set_email(self, email: str):
        self.__email = email
        return self

    def set_phone(self, phone: str):
        self.__phone = phone
        return self

    def build(self) -> Customer:
        return Customer(self.__id, self.__firstname, self.__lastname, self.__email, self.__phone)
