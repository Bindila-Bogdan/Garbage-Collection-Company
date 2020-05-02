class Account:
    account_type = "Cont"

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_username(self, new_username):
        self.__username = new_username
        print("New username was set to: " + new_username + ".")

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password
        print("New password was set to: " + new_password + ".")

    def get_account_type(self):
        return self.account_type
