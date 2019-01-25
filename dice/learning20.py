# class - this is a blueprint of an object

import random
import bankaccount.BankAccount

class Dice:

    # this is the method executed when an object is created
    # Shift+F6 is for renaming any variable, function or class anything - keyboard shortcut
    def __init__(self):
        print("creating of the object is done here")
        self.dice_face_up = 6;
        # print(self)
        # self.db_connection = db_connection
        pass

    def roll_dice(self):
        self.dice_face_up = random.randint(1, 6)
        # print(self)
        pass


    # def get_data_from_db(self):
        # self.db_connection.connect()

print("creating an object")
d = Dice() # this is where you are creating an object and assigining the object to d variable
print(d)
# Dice d = new Dice();
print("callig the roll_dice function: Iteration :1")
d.roll_dice() # at this instance only self will have d object
print(d.dice_face_up)

print("callig the roll_dice function: Iteration :2")
d.roll_dice()
print(d.dice_face_up)

# print("callig the roll_dice function: Iteration :3")
# d.roll_dice()
# print(d.dice_face_up)

savingsAcc = bankaccount.BankAccount.BankAccount(89734)
print(savingsAcc)
# print("creating the second object")
# d2 = Dice()
# print(d2)
# print("calling the roll_dice function for second object")
# d2.roll_dice() # at this instance only self will have d2 object
# print(d2.dice_face)

# 1.


# class Employee {
#     // constructor
#     public Employee(int noOfEmployees) {
#         this.
#         numberOfEmployee= noOfEmployees;
#     }
#     int numberOfEmployee;
# }
#
# Employee d = new Employee(10);