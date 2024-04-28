class BankAccount:
    def __init__(self, username, password, authenticated=False):
        self.balance = 0
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def authenticate(self, username, password):
        if self.password == password and self.username == username:
            self.authenticated = True
            return True
        else:
            print("authenticate failed")
            self.authenticated = False
            return False

    def deposit(self, amount, username, password):
        if self.authenticate(username, password) == True:
            if amount <= 0:
                raise ValueError("Deposit amount must be a positive integer.")
            else:
                self.balance += amount
                print(f"Deposit successful. New balance: {self.balance}")
        else:
            raise ValueError("authentication failed ")

    def withdraw(self, amount, username, password):
        if self.authenticate(username, password) == True:
            if amount <= 0:
                raise ValueError("Withdraw amount must be a positive integer.")
            else:
                self.balance -= amount
                print(f"Withdraw successful. New balance: {self.balance}")
        else:
            raise ValueError("authentication failed ")

    def __str__(self):
        return f"Username:{self.username}\nBalance: {self.balance}"


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, authenticated=False, minimum_balance=0):
        super().__init__(username, password)
        self.minimum_balance = minimum_balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def withdraw(self, amount, username, password):
        if self.authenticate(username, password):
            if amount <= 0:
                raise ValueError("Withdraw amount must be a positive integer.")
            elif self.balance - amount < self.minimum_balance:
                raise ValueError("Your balance must remain higher than or equal to the minimum balance.")
            else:
                self.balance -= amount
                print(f"Withdraw successful. New balance: {self.balance}")
        else:
            raise ValueError("Authentication failed")


def main():
    my_banc_account = BankAccount("Maria", "123456789m")
    print(my_banc_account)
    my_banc_account.deposit(2000, "Maria", "123456789m")
    my_banc_account.withdraw(100, "Maria", "123456789m")
    my_new_account = MinimumBalanceAccount("Elena", "123456789m", False, 500)
    print(my_new_account)
    my_new_account.deposit(3000, "Elena", "123456789m")
    my_new_account.withdraw(2700, "Elena", "123456789m")


if __name__ == "__main__":
    main()
