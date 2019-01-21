# dettach and fileno
#
import traceback

try:
    f = open('somefile_2.txt', 'r')
    print(f.read()) # will throw an exception
    f.close()
except Exception as e:
    print(e)
    print(traceback.format_exc())

#Exception - parent of all the exception or error classes

# IndexError

# ValueError

# ZeroDivisionError

# ArithmeticError




print("After Exception occurred")
# print("=========================================================")
# f = open('python-first-class.txt', 'r')
# print(f.readlines())
# for c in f.readlines():
#     print(c)

#f.write("This is the new file text")




# for line in f.readlines():
#     print(line)