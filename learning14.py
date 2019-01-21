import traceback


# def method1():
#     try:
#         name = "Python Programming"
#         for i in range(25):
#             print(name[i], end='')
#     except IndexError as e:
#         print()
#         # print(e)
#         # print(traceback.format_exc())
#         raise IndexError()
        # raise IndexError("The length of provided String is greater than what is expected. Please povide a string with 18 characters only")


# try:
#     method1()
# except Exception as e:
#     print(e)
#     print(traceback.format_exc())

#try/except with an else case

# try:
#     number = int(input("please enter a number:"))
#     print("the number is ", number)
# except: # generic exception suite
#     print("some exception occurred")
# else:
#     print("Otherwise everything is seems to be good")

try:
    number = int(input("please enter a number"))
    # f = open("somefile.txt")
    print("the number is ", number)
    # you got an exception here
    # f.close()
except:
    print("some exception occurred")
finally:
    # f.close()
    number = None
    # this clause is used for cleanup activities
    print("this executed irrespective of exception")
