from model.generic_employee import GenericEmployee


class Administrator(GenericEmployee):
    def __init__(self, first_name, last_name, account):
        super().__init__(first_name, last_name)
        self.__administrator_account = account

    def get_account(self):
        return self.__administrator_account
