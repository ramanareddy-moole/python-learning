class BankAccount:

    # this is mandatory by standard of python
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        return self.__balance;

    def withdraw(self, amount):
        # self.__balance -= amount # short hand assignments -=, +-
        if amount > self.__balance:
            print("Error: insufficient balance")
        else:
            self.__balance = self.__balance - amount

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def __str__(self):
        return "Bank Account with balance " + str(self.__balance)