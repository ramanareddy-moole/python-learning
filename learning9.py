# Functions
# Files
# Collections

# Functions - a set of instructions, which can be executed on demand

# def is keyword
# function_name is a any name what the function is trying to achieve

#def function_name(arg1, arg2 , arg3...):
#    statement1
#    statement2
#    statement3
#    ...
#    ...
#    return value

# custom functions

def get_discounted_price(d, ap):
    discounted_price = ap - (ap * d/100)
    return discounted_price


def non_returning_func():
    print("this function doesnt return anything")


def return_string(d, ap):
    discounted_price = ap - (ap * d/100)
    return "the discouned price is " + str(discounted_price)


# these are default value based arguments
def function1(name="Aditya", location="Andhra Pradesh"):
    return name + "," + location


print(function1()) # not passing any input arguments
print(function1("Hema", "Telangana"))
print(function1("Ramana"))
print(function1(location="United States", name="Maximus Decimus"))

# discount = float(input("enter the discout percentage :"))
# actual_price = float(input("please enter the actual price :"))
#
# print(get_discounted_price(discount, actual_price))
# non_returning_func()
# print(return_string(discount, actual_price))