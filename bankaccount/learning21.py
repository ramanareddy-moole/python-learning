# bank account
# balance, deposits and withdrawals


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

print("We are going to work with bank account")

b = int(input("Please enter some starting balance for savings account"))
savingsAcc = BankAccount(b) # the  value 1000 is equal to the balance argument of __init__ function
print(savingsAcc)

cb = int(input("please enter some starting balance for current account"))
currentAcc = BankAccount(cb)
print(currentAcc)
print("the balance in your account :", savingsAcc.show_balance())

d = int(input("please enter deposit value:"))
savingsAcc.deposit(d) # here d value is equal to amount argument in deposit function

print("the balance in your account :", savingsAcc.show_balance())

w = int(input("please enter withdrawl value:"))
savingsAcc.withdraw(w) # here w value is equal to amount argument in withdraw function

print("the balance in your account :", savingsAcc.show_balance())

