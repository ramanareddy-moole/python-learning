
import traceback

try:
    number1 = int(input("enter number 1")) # ValueError
    number2 = int(input("enter number 2"))

    if number2 != 0:
        number3 = number1/number2
        print("the division :", number3)
    else:
        print("Please enter a proper value")
except Exception as e:
    print(e)
# ZeroDivisionError as e:
#     print(e)
#     print(traceback.format_exc()) # this will print the total stack trace of the program with line numbers
# except ValueError as e:
#     print(e)
#     print(traceback.format_exc())

print("After Exception occurred")