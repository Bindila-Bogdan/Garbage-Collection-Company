from model.employee import Employee
from model.coordinator import Coordinator
from model.administrator import Administrator


class EmployeeFactory:
    @staticmethod
    def obtain_employee(first_name, last_name, account, type_of_employee):
        type_of_employee = type_of_employee.capitalize()
        if type_of_employee == "Employee":
            return Employee(first_name, last_name, account)
        elif type_of_employee == "Coordinator":
            return Coordinator(first_name, last_name, account)
        elif type_of_employee == "Administrator":
            return Administrator(first_name, last_name, account)
        else:
            print("Inexistent type.")
            return None
