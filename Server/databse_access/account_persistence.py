from databse_access.manager import Manager
from mysql.connector.errors import IntegrityError
from databse_access.persistence import Persistence
from model.account import Account
from model.employee_account import EmployeeAccount
from model.coordinator_account import CoordinatorAccount
from model.administrator_account import AdministratorAccount


class AccountPersistence(Persistence):
    def __init__(self):
        super().__init__("Account_Persistence")
        self.__accounts = {}

    @staticmethod
    def add_account(account_username, account_password):
        account_data = (account_username, account_password)
        connection, cursor = Manager.connect()
        insert_account_statement = """INSERT INTO account (username, password) VALUES (%s, %s)"""
        try:
            cursor.execute(insert_account_statement, account_data)
            connection.commit()
        except IntegrityError:
            pass
        connection.close()

    @staticmethod
    def delete_account(current_id):
        current_id = str(current_id)
        connection, cursor = Manager.connect()
        delete_account_statement = "DELETE FROM account WHERE id = " + current_id
        cursor.execute(delete_account_statement)
        connection.commit()
        connection.close()

    @staticmethod
    def update_password(current_id, new_password):
        connection, cursor = Manager.connect()
        update_password_statement = "UPDATE account SET password = %s WHERE id = %s"
        values = (new_password, current_id)
        cursor.execute(update_password_statement, values)
        connection.commit()
        connection.close()

    @staticmethod
    def update_username(account_id, new_username):
        connection, cursor = Manager.connect()
        update_username_statement = "UPDATE account SET username = %s WHERE id = %s"
        values = (new_username, account_id)
        cursor.execute(update_username_statement, values)
        connection.commit()
        connection.close()

    @staticmethod
    def get_account_id(account_username, account_password):
        connection, cursor = Manager.connect()
        get_account_id_statement = "SELECT id FROM account WHERE username = %s and password = %s"
        values = (account_username, account_password)
        cursor.execute(get_account_id_statement, values)
        ids = cursor.fetchall()
        connection.close()
        return ids

    @staticmethod
    def display_accounts():
        connection, cursor = Manager.connect()
        get_accounts_statement = "SELECT * FROM account"
        cursor.execute(get_accounts_statement)
        accounts = cursor.fetchall()
        connection.close()
        for account in accounts:
            print(account)

    def get_data(self):
        connection, cursor = Manager.connect()
        get_accounts_statement = "SELECT * FROM account"
        cursor.execute(get_accounts_statement)
        accounts = cursor.fetchall()
        connection.close()
        for account in accounts:
            self.__accounts[account[0]] = Account(account[1], account[2])
        return self.__accounts

    @staticmethod
    def get_account_with_id(account_id, employee):
        account_id = str(account_id)
        connection, cursor = Manager.connect()
        get_account_id_statement = "SELECT * FROM account WHERE id = " + account_id
        cursor.execute(get_account_id_statement)
        account = cursor.fetchall()
        connection.close()
        if employee:
            return EmployeeAccount(account[0][1], account[0][2], False)
        elif employee is not None:
            return CoordinatorAccount(account[0][1], account[0][2], False)
        else:
            return AdministratorAccount(account[0][1], account[0][2], False)
