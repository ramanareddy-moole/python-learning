# generate the username based on firstname, lastname and Id
# first three charactes of firstname
# first three characters of lastname
# last three characters of ID
# FN: Aditya LN: Chaluvadi and ID: 8745323 --> adicha323

first_name = input("please enter firstname :")
last_name = input("please enter lastname:")
id = input("please enter ID value")

#0-4 - 0, 1, 2, 3
#0-3 - 0, 1, 2
# 8745323

username1 = first_name[:3]
username2 = last_name[:3]
username3 = id[-3:]  # -3, -2, -1

generated_user = username1 + username2 + username3
print("The Generated username for :", first_name, last_name, id)
print(generated_user)