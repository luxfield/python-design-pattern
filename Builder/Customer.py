class Customer:

    def __init__(self, id, firstname, lastname, email, phone) -> None:
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__phone = phone

        print(
            f'ID: {self.__id} \nNama Depan {self.__firstname} \nNama Belakang {self.__lastname} \nSurel {self.__email} \nTelepon {self.__phone}')

    def get_id(self) -> str:
        return self.__id

    def get_firstname(self) -> str:
        return self.__firstname

    def get_lastname(self) -> str:
        return self.__lastname

    def get_email(self) -> str:
        return self.__email

    def get_phone(self) -> str:
        return self.__phone
