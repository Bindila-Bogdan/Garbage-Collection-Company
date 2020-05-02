from model.generic_employee import GenericEmployee


class Coordinator(GenericEmployee):
    def __init__(self, first_name, last_name, account):
        super().__init__(first_name, last_name)
        self.__coordinator_account = account

    def get_account(self):
        return self.__coordinator_account
