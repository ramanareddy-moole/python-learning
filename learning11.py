# modules
# math and random

# the import statement mean that, we would like to import all the functions, classes to be loaded into our program
import random
import math

# print(random.randint(1, 10)) # this method includes the starting ang ending values

# print(random.randrange(1, 10)) # this method will not include the end point (10)

# for i in range(10):
#     print(random.randrange(1, 10))

MIN = 1
MAX = 6

proceeed = 'y'

# assume that two persons are throwing dice
while proceeed == 'y':
    name1 = input("please enter your name to throw dice")
    dice1 = random.randint(MIN, MAX)

    name2 = input("please enter yout name to throw dice")
    dice2 = random.randint(MIN, MAX)

    print(name1, "your dice value is", dice1)
    print(name2, "your dice value is", dice2)
    if dice1 > dice2:
        print(name1, "won the lucky dice competition")
    else:
        print(name2, "won the lucky dice competition")

    proceeed = input("do you want to play the dice competition again? (press y to play again)")
else:
    print("The lucky dice competition is ended")