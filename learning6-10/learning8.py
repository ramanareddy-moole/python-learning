
# demo on ILDE and help function
# break and continue
# More about Strings, positive index, negative index, IndexError Exceptions, len(), split(), lower(), upper()
# count character example
# String slicing

# print("Ramana", "Reddy", "moola", end='')
# print("I love my village")

# f = open("somefile.txt", "w") # opening a file in write mode
# print('I would love to do farming', file=f)

# for i in range(10): # iterating the loop for 10 times
#     print("i value is ", i)
#     break
    # if i == 5: # when i value is 5 i want to the break
    #     print("breaking the loop as the i value is 5")
    #     break

# for i in range(10):  # iterating the loop for 10 times
#     print("i value is ", i)
#     continue
#     print("after continue statement")

# break - this stops the execution of the loop itself
# continue - this will let the execution of the loop but it will not execute any statements you keep after the continue

# name = "Ramana Reddy"

# print("name in double quotes :", name)

# name = 'Ramana Reddy'
# print("name in single quotes :", name)

# """This can also be used as multi-line comments"""
# '''
# This is also a multi-line comment
# '''
# print("name in three double quotes :", name)

# for c in name:
#     print(c)

#print("printing with range function")
# for i in range(len(name)):
#     print(name[i], end='') #0-length of the string

# negative index
#"Ramana" - 0 to 5

#"Ramana" - -6 to -1
# name = "Ramana"
# print(list(range(0, len(name), -1)))
# for i in range(0, len(name), -1):
#     print(name[i], end='')

# name[-7]

# l = [1, 2, 3, 4, 5]
# len(l)
# for i in l:
#     print(i)

# name = "Ram-ana"
# print(name.upper())
# print(name.lower())
# print(name.split(sep='-'))


# count characters
# statement = "I want to watch Fun and Fustration movie tonight"

# count = 0
# for c in statement:
#     if c == 'T' or c == 't':
#         count = count + 1


# print("the number of Ts in the statement is ", count)

name = input("enter a string:")

# for i in range(0, len(name)):
#     print(name[i], end=' ')

# print()
# print("Reverse string printing now")
# range(1, 9) - 1, 2, 3, 4, 5, 6, 7, 8
# range(10) - 1-9
#SPARROW - 7

# print(list(range(-1, -7)))

# for i in range(-1, -(len(name) + 1), -1):
#     print(name[i], end=' ')


print(name[1:5])
# start:end:step
# Strings, list set, tuples

print(name[-1: -(len(name) + 1): -1])

print(name[:])

print(name[:3]) # 0-2
print(name[2:]) # 2-LEN(NAME)-1