# for

# while  - indefinite number of iterations
# for - when you have definite number of iterations
# range function will return numbers from 0-the value specified minus 1, 0-9
range5 = range(5)
range9 = range(9)
range215 = range(2, 15)
range4202 = range(4, 20, 2)
print(range5) # starts from zero until the number-1
print(list(range9)) #
print(list(range215)) # starts with 2 and ends before 15
print(list(range4202)) # starts with 4, 6, 8, 10, 12, ....18

# for i in range4202:
#     print("iteration ", i)