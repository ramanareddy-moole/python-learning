# Datatypes and type conversions
# decision statments such if, nested if, if..elif and for and while while..else and break continue and pass

# String name = "Aditya"; # java or c
name = "Bengaluru"
number = "7634234"
binary = "10101"
f = "13.452"
n = 121
d = 23.34
b = True

print(float(f) * 4)

# * is replication when you multiply a string value with integer
# * will multiply mathematically if both the operands are similar type

decimal = int(number, 10)

# + if you have two string operands then cancatenation
# + if you have any int or float then it will be a mathematical addition

print(decimal) # decimal, octa, hexadcimal and binary numbers

print("Octa number is :" + str(int(number, 8)))
print("hexadecimal number is :" + str(int(number, 16)))
print("Binary number is :" + str(int(binary, 2)))

x = n + d # addition
print(x)
a = int(number) + 3 # concatenation . . . 76342343 or 7634237
print("addition :" + str(a))

#try: # i may have exceptions but i dont want to stop my program from running instead i want t continue by an error message which s understable to a programmer
#print(int(name))
#except ValueError as e:
#    print("unable to parse the value", e)

print("after try statement")
#print(a)
#print(d)
#print(b)