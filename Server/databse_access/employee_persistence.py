from databse_access.account_persistence import AccountPersistence
from mysql.connector.errors import IntegrityError
from model.employee_account import EmployeeAccount
from model.coordinator_account import CoordinatorAccount
from databse_access.database_manager import DatabaseManager
from databse_access.persistence import Persistence
from model.employee_factory import EmployeeFactory
from model.administrator_account import AdministratorAccount


class EmployeePersistence(Persistence):
    def __init__(self):
        super().__init__("Employee_Persistence")
        self.__employees = []
        self.__coordinators = []
        self.__administrators = []

    @staticmethod
    def add_employee(first_name, last_name, employee):
        if employee:
            account = EmployeeAccount(first_name + "_" + last_name, "default", True)
        elif employee is not None:
            account = CoordinatorAccount(first_name + "_" + last_name, "default", True)
        else:
            account = AdministratorAccount(first_name + "_" + last_name, "default", True)

        account_username = account.get_username()
        account_password = account.get_password()
        AccountPersistence.add_account(account_username, account_password)
        ids = AccountPersistence.get_account_id(account_username, account_password)

        connection, cursor = DatabaseManager.connect()

        data = (first_name, last_name, ids[0][0])
        if employee:
            insert_statement = """INSERT INTO employee (first_name, last_name, account_id) 
                                               VALUES (%s, %s, %s)"""
        elif employee is not None:
            insert_statement = """INSERT INTO coordinator (first_name, last_name, account_id) 
                                                          VALUES (%s, %s, %s)"""
        else:
            insert_statement = """INSERT INTO administrator (first_name, last_name, account_id) 
                                                                      VALUES (%s, %s, %s)"""

        try:
            cursor.execute(insert_statement, data)
        except IntegrityError:
            pass
        connection.commit()
        connection.close()

    @staticmethod
    def delete_employee(first_name, last_name, employee):
        if employee is False and employee is not None:
            connection, cursor = DatabaseManager.connect()
            delete_coordinator_statement = "UPDATE employee SET coordinator_first_name = %s, " + \
                                           "coordinator_last_name = %s WHERE coordinator_first_name = %s " \
                                           "AND coordinator_last_name = %s"
            values = (None, None, first_name, last_name)
            cursor.execute(delete_coordinator_statement, values)
            connection.commit()
            connection.close()

        connection, cursor = DatabaseManager.connect()
        get_account_id_statement = "SELECT account_id FROM employee WHERE first_name = %s and last_name = %s"
        values = (first_name, last_name)
        cursor.execute(get_account_id_statement, values)
        ids = cursor.fetchall()

        if employee:
            delete_statement = "DELETE FROM employee WHERE first_name = %s and last_name = %s"
        elif employee is not None:
            delete_statement = "DELETE FROM coordinator WHERE first_name = %s and last_name = %s"
        else:
            delete_statement = "DELETE FROM administrator WHERE first_name = %s and last_name = %s"

        values = (first_name, last_name)
        cursor.execute(delete_statement, values)
        connection.commit()
        connection.close()
        if len(ids) == 0:
            return
        AccountPersistence.delete_account(ids[0][0])

    def update_employee(self, first_name, last_name, new_first_name, new_last_name, employee):
        employees = None
        if employee is False:
            employees = self.get_coordinated_employees(first_name, last_name)
            for emp in employees:
                self.remove_coordinator(emp[0], emp[1])

        connection, cursor = DatabaseManager.connect()
        if employee:
            update_statement = "UPDATE employee SET first_name = %s, " + \
                               "last_name = %s WHERE first_name = %s AND last_name = %s"
        elif employee is not None:
            update_statement = "UPDATE coordinator SET first_name = %s, " + \
                               "last_name = %s WHERE first_name = %s AND last_name = %s"
        else:
            update_statement = "UPDATE administrator SET first_name = %s, " + \
                               "last_name = %s WHERE first_name = %s AND last_name = %s"

        values = (new_first_name, new_last_name, first_name, last_name)
        cursor.execute(update_statement, values)
        connection.commit()
        connection.close()

        if employee is False and employees is not None:
            for emp in employees:
                self.set_coordinator(emp[0], emp[1], new_first_name, new_last_name)

        self.set_new_username(new_first_name, new_last_name, employee)

    @staticmethod
    def set_new_username(new_first_name, new_last_name, employee):
        connection, cursor = DatabaseManager.connect()
        if employee:
            get_account_id_statement = "SELECT account_id FROM employee WHERE first_name = %s AND last_name = %s"
        elif employee is not None:
            get_account_id_statement = "SELECT account_id FROM coordinator WHERE first_name = %s AND last_name = %s"
        else:
            get_account_id_statement = "SELECT account_id FROM administrator WHERE first_name = %s AND last_name = %s"

        values = (new_first_name, new_last_name)
        cursor.execute(get_account_id_statement, values)
        ids = cursor.fetchall()
        connection.close()

        if employee:
            new_username = "employee_" + new_first_name + "_" + new_last_name
        elif employee is not None:
            new_username = "coordinator_" + new_first_name + "_" + new_last_name
        else:
            new_username = "administrator_" + new_first_name + "_" + new_last_name
        AccountPersistence.update_username(ids[0][0], new_username)

    @staticmethod
    def set_new_password(first_name, last_name, new_password, employee):
        connection, cursor = DatabaseManager.connect()
        if employee:
            get_account_id_statement = "SELECT account_id FROM employee WHERE first_name = %s AND last_name = %s"
        elif employee is not None:
            get_account_id_statement = "SELECT account_id FROM coordinator WHERE first_name = %s AND last_name = %s"
        else:
            get_account_id_statement = "SELECT account_id FROM administrator WHERE first_name = %s AND last_name = %s"

        values = (first_name, last_name)
        cursor.execute(get_account_id_statement, values)
        ids = cursor.fetchall()
        connection.close()
        AccountPersistence.update_password(ids[0][0], new_password)

    @staticmethod
    def set_coordinator(first_name, last_name, coordinator_fist_name, coordinator_last_name):
        connection, cursor = DatabaseManager.connect()
        update_employee_statement = "UPDATE employee SET coordinator_first_name = %s, " + \
                                    "coordinator_last_name = %s WHERE first_name = %s AND last_name = %s"
        values = (coordinator_fist_name, coordinator_last_name, first_name, last_name)
        try:
            cursor.execute(update_employee_statement, values)
        except IntegrityError:
            pass
        connection.commit()
        connection.close()

    @staticmethod
    def remove_coordinator(first_name, last_name):
        connection, cursor = DatabaseManager.connect()
        update_employee_statement = "UPDATE employee SET coordinator_first_name = %s, " + \
                                    "coordinator_last_name = %s WHERE first_name = %s AND last_name = %s"
        values = (None, None, first_name, last_name)
        cursor.execute(update_employee_statement, values)
        connection.commit()
        connection.close()

    @staticmethod
    def set_location(first_name, last_name, location_name):
        if location_name is None:
            EmployeePersistence.remove_location(first_name, last_name)
        connection, cursor = DatabaseManager.connect()
        update_employee_statement = "UPDATE employee SET loc_id = %s " + \
                                    "WHERE first_name = %s AND last_name = %s"
        values = (location_name, first_name, last_name)
        try:
            cursor.execute(update_employee_statement, values)
        except IntegrityError:
            pass
        connection.commit()
        connection.close()

    @staticmethod
    def remove_locations_from_employees(location_name):
        connection, cursor = DatabaseManager.connect()
        get_employee_statement = "SELECT first_name, last_name FROM employee WHERE loc_id =" + location_name
        cursor.execute(get_employee_statement)
        employees = cursor.fetchall()
        connection.close()
        for employee in employees:
            EmployeePersistence.remove_location(employee[0], employee[1])

    @staticmethod
    def remove_location(first_name, last_name):
        connection, cursor = DatabaseManager.connect()
        update_employee_statement = "UPDATE employee SET loc_id = %s " + \
                                    "WHERE first_name = %s AND last_name = %s"
        values = (None, first_name, last_name)
        cursor.execute(update_employee_statement, values)
        connection.commit()
        connection.close()

    @staticmethod
    def get_coordinated_employees(coordinator_first_name, coordinator_last_name):
        connection, cursor = DatabaseManager.connect()
        get_coordinated_employees_statement = "SELECT * FROM employee WHERE coordinator_first_name = %s AND" + \
                                              " coordinator_last_name = %s"
        values = (coordinator_first_name, coordinator_last_name)
        cursor.execute(get_coordinated_employees_statement, values)
        employees = cursor.fetchall()
        connection.close()
        return employees

    @staticmethod
    def display_employees():
        connection, cursor = DatabaseManager.connect()
        get_employees_statement = "SELECT * FROM employee"
        cursor.execute(get_employees_statement)
        employees = cursor.fetchall()
        connection.close()
        for employee in employees:
            print(employee)

    @staticmethod
    def display_coordinators():
        connection, cursor = DatabaseManager.connect()
        get_coordinators_statement = "SELECT * FROM coordinator"
        cursor.execute(get_coordinators_statement)
        coordinators = cursor.fetchall()
        connection.close()
        for coordinator in coordinators:
            print(coordinator)

    @staticmethod
    def display_administrators():
        connection, cursor = DatabaseManager.connect()
        get_administrators_statement = "SELECT * FROM administrator"
        cursor.execute(get_administrators_statement)
        administrators = cursor.fetchall()
        connection.close()
        for administrator in administrators:
            print(administrator)

    def get_data(self, print_employees=False):
        all_employees = []
        for employee in self.get_employees():
            all_employees.append(employee)
        for coordinator in self.get_coordinators():
            all_employees.append(coordinator)
        for administrator in self.get_administrators():
            all_employees.append(administrator)
        if print_employees:
            for employee in all_employees:
                print(employee.get_first_name() + " " + employee.get_last_name())
                print(employee.get_account().get_username() + " " + employee.get_account().get_password())
                print(employee.get_account().get_account_type() + "\n")
        return all_employees

    def get_employees(self):
        self.__employees = []
        connection, cursor = DatabaseManager.connect()
        get_employees_statement = "SELECT * FROM employee"
        cursor.execute(get_employees_statement)
        employees = cursor.fetchall()
        connection.close()
        for employee in employees:
            account = AccountPersistence.get_account_with_id(employee[5], True)
            retrieved_employee = EmployeeFactory.obtain_employee(employee[0], employee[1], account,
                                                                 "Employee")
            if employee[2] is not None and employee[3] is not None:
                retrieved_employee.assign_coordinator(employee[2] + " " + employee[3])
            retrieved_employee.assign_location(employee[4])
            self.__employees.append(retrieved_employee)
        return self.__employees

    def get_coordinators(self):
        self.__coordinators = []
        connection, cursor = DatabaseManager.connect()
        get_coordinators_statement = "SELECT * FROM coordinator"
        cursor.execute(get_coordinators_statement)
        coordinators = cursor.fetchall()
        connection.close()
        for coordinator in coordinators:
            account = AccountPersistence.get_account_with_id(coordinator[2], False)
            retrieved_coordinator = EmployeeFactory.obtain_employee(coordinator[0], coordinator[1], account,
                                                                    "Coordinator")
            self.__coordinators.append(retrieved_coordinator)
        return self.__coordinators

    def get_administrators(self):
        self.__administrators = []
        connection, cursor = DatabaseManager.connect()
        get_administrator_statement = "SELECT * FROM administrator"
        cursor.execute(get_administrator_statement)
        administrators = cursor.fetchall()
        connection.close()
        for administrator in administrators:
            account = AccountPersistence.get_account_with_id(administrator[2], None)
            retrieved_administrator = EmployeeFactory.obtain_employee(administrator[0], administrator[1], account,
                                                                      "Administrator")
            self.__administrators.append(retrieved_administrator)
        return self.__administrators
