# lets look into collections - list, set, dict, tuples
# classes
# inheritance

number = 12
name = "Aditya"
l = []
# print(l)

# A list is a variable which contains multiple values
l = [1, 2, 3, 4, 5]
# print(l)

l = list() # another way of initializing a list
# print(l)

l = [1, 2, 3, "Ramana", "Reddy", 10.2, 234, "United States"] # 0-5 indices
# print(l)

# print(l[3]) # print the value at index 3 . . . the index starts from 0
# print(l[6]) # this ihe ndex is not available in the list . . so throws an IndexError

# print(int(l[3]))

# for i in range(6): # 0-5 values
#     print("list with index:", i, " value :", l[i])
#
# print("Iterating using length")
# # print(len(l))
#
# for i in range(len(l)):
#     print("list with index:", i, " value :", l[i])

l[2] = "Maximus" # reassign a value at an indx with different value
# print(l)

# l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = ["Name1", "Name2", "Name3", "Name4", "Name5", 6, 7, 8, 9, 10]

# print(l[1:3]) # this is going to return the values from indices 1-2
# print(l2[0:5]) # prints values from 0-4 index

# print(l2[::4]) # 1, 3, 5, 7, 9
# print(l2[1:15:2]) #

# l2.append()
# l2.remove()
# l2.index("Name2")

l_multi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(type(l_multi[0]))
# for i in range(len(l_multi)):
#     print(l_multi[i])
#     for j in range(len(l_multi[i])):
#         print(l_multi[i][j])

def customSort(e):
    return len(e)

names = ["Google", "Microsoft", "Facebook", "Instagram", "ABC", "Cisco"]

print("Before sort")
print(names)

names.sort()
print("After sort")
print(names)

names.sort(reverse=True)
print(names)

names.sort(key=customSort)

print(names)
#print(l_multi)