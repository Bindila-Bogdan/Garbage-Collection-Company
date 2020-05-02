from model.employee import Employee
from model.coordinator import Coordinator


class EmployeesProcessing:
    def __init__(self, server_communication):
        self.__employees = []
        self.__server_communication = server_communication

    def set_employees(self, employees):
        self.__employees = employees

    def get_coordinators(self):
        coordinators = []
        for employee in self.__employees:
            if isinstance(employee, Coordinator):
                coordinators.append(employee)
        return coordinators

    def search_employee(self, first_name, last_name):
        for employee in self.__employees:
            if employee is not None:
                if employee.get_last_name() == last_name and employee.get_first_name() == first_name:
                    return True
        return False

    def check_if_coordinator_exits(self, coordinator_name):
        for employee in self.__employees:
            if employee is not None:
                if isinstance(employee, Coordinator):
                    if employee.get_first_name() + " " + employee.get_last_name() == coordinator_name:
                        return True
        return False

    @staticmethod
    def retrieve_employee(first_name, last_name, role, employees):
        if role.lower() == "employee" or role.lower() == "coordinator":
            for employee in employees:
                if employee is not None:
                    if (isinstance(employee, Employee) and role.lower() == "employee") or \
                            (isinstance(employee, Coordinator) and role.lower() == "coordinator"):
                        if employee.get_first_name() == first_name and employee.get_last_name() == last_name:
                            return employee
            return None
        else:
            return None

    def search_for_account(self, username, password):
        for employee in self.__employees:
            if employee is not None:
                account = employee.get_account()
                if account.get_username() == username and account.get_password() == password:
                    return account, employee
        return None, None

    def get_coordintated_employees(self, coordinator):
        list_of_coordinated_employees = []
        for employee in self.__employees:
            if employee is not None:
                if isinstance(employee, Employee) and (employee.get_coordinator() == coordinator):
                    list_of_coordinated_employees.append(employee)
        return list_of_coordinated_employees

    def get_accounts(self):
        accounts = []
        for employee in self.__employees:
            if employee is not None:
                accounts.append(employee.get_account())
        return accounts

    def get_employees(self):
        non_empty_employees = []
        for employee in self.__employees:
            if employee is not None:
                non_empty_employees.append(employee)
        return non_empty_employees

    def get_just_employees(self):
        non_empty_employees = []
        for employee in self.__employees:
            if employee is not None:
                if isinstance(employee, Employee):
                    non_empty_employees.append(employee)
        return non_empty_employees

    def assign_location(self, first_name, last_name, location_name):
        data = [first_name, last_name, location_name]
        updated_data = self.__server_communication.communicate(4, data)
        self.__employees = updated_data[0]

    def display_employees(self):
        for employee in self.__employees:
            print(employee.get_first_name() + " " + employee.get_last_name())
            print(employee.get_account().get_username() + " " + employee.get_account().get_password())

    def update_password(self, first_name, last_name, new_password, employee):
        data = [first_name, last_name, new_password, employee]
        updated_data = self.__server_communication.communicate(0, data)
        self.__employees = updated_data[0]

    def add_employee(self, first_name, last_name, employee):
        data = [first_name, last_name, employee]
        updated_data = self.__server_communication.communicate(5, data)
        self.__employees = updated_data[0]

    def assign_coordinator(self, first_name, last_name, coordinator_first_name, coordinator_last_name):
        data = [first_name, last_name, coordinator_first_name, coordinator_last_name]
        updated_data = self.__server_communication.communicate(6, data)
        self.__employees = updated_data[0]

    def remove_employee(self, first_name, last_name, employee):
        data = [first_name, last_name, employee]
        updated_data = self.__server_communication.communicate(7, data)
        self.__employees = updated_data[0]

    def modify_employee(self, first_name, last_name, new_first_name, new_last_name, employee):
        data = [first_name, last_name, new_first_name, new_last_name, employee]
        updated_data = self.__server_communication.communicate(8, data)
        self.__employees = updated_data[0]
