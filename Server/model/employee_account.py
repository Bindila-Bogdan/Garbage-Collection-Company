from model.account import Account


class EmployeeAccount(Account):
    account_type = "employee"

    def __init__(self, username, password, creation):
        if creation:
            super().__init__(self.account_type + "_" + username, self.account_type + "_" + password)
        else:
            super().__init__(username, password)
