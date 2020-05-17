from model.generic_employee import GenericEmployee


class Employee(GenericEmployee):
    def __init__(self, first_name, last_name, account):
        super().__init__(first_name, last_name)
        self.__coordinator = None
        self.__location = None
        self.__employee_account = account

    def get_account(self):
        return self.__employee_account

    def assign_coordinator(self, coordinator):
        self.__coordinator = coordinator

    def get_coordinator(self):
        if self.__coordinator is None:
            return "-"
        else:
            return self.__coordinator

    def assign_location(self, location_name):
        self.__location = location_name

    def get_location(self):
        if self.__location is None:
            return "Not assigned"
        else:
            return self.__location
