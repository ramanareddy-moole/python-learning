object = [{"name":"Aditya", "salary": "121212", "hours": 40, "payrate": 60},
          {"name": "Ramana", "salary": "324223", "hours": 40, "payrate" : 10},
          {"name": "Hema", "salary": "827342", "hours": 35, "payrate": 73},
          {"name":"Sagar", "salary": "726342", "hours":34, "payrate": 84}]

print("before sorted object :", object)
def customSortFunction(e):
    # in this mehod you can perform any processing, but this method should always return a value (String or number)
    return e["hours"] * e["payrate"]
    # return e["salary"]

object.sort(key=customSortFunction, reverse=True)
print("Sorted Object : ", object)

l = [1, 2, 3]

print(l * 3)

name = "Ramana" * 4
print(name)

number = 10*20
print(number)

#operator overloading
#+ - you can use for summing the numbers
#    you can use for concatenating strings

#* - you can use for multiplication of numbers
#  - you can use for repeating the sequence
