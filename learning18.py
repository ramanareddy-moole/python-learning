#Dictionaries

# PId name   price     discount avlblCnt creatdate
# 1 | moto | 5000.000 | -6 | 2015 - 06 - 18 11: 26:54 |
# # 2 | sony | 7000.000 | 10 | 2015 - 04 - 08 17: 31:15
# # 3 | nokia | 10000.000 | 65 | 2015 - 04 - 08 17: 31:22
# # 4 | htc | 9999.000 | 21 | 2015 - 04 - 08 17: 31:26
# # 5 | htc | 15000.000 | 0 | 2015 - 04 - 08 17: 31:29
# # 12 | moto | 5000.000 | 4 | 2015 - 01 - 24 17: 58:26


# record1 = [721, 1, "moto", 5000, -6, "2015 - 06 - 18 11: 26:54"]
# record2 = [2, "sony", 7000.000, 10, "2015 - 04 - 08 17: 31:15"]
# record3 = [3, "nokia", 10000.000 , 65, "2015 - 04 - 08 17: 31:22"]
# print(record1[0]) # we expected this to print pId

drecord1 = {"parentId": 721, "pId":1, "name": "moto", "avlbcnt": -6, "createdate0": "2015 - 06 - 18 11: 26:54"}
drecord2 = {"pId":2, "name": "sony", "avlbcnt": 4, "createdate0": "2015 - 06 - 18 11: 26:54"}
drecord3 = {"pId":3, "name": "nokia", "avlbcnt": 121, "createdate0": "2015 - 06 - 18 11: 26:54"}

dr = dict([("parentId", 721), ("pId", 1), ("name","moto"), ("name", "nokia")])

# dr = dict({"parentId":721, "pId":1})

# print(dr)

# print(dr.keys()) # this will return a set of all the keys in a dictionary
# print(dr.values()) # this wil return all the values

for key in dr:
    print(key, dr[key])

print("Iterating the dictionary using tuple")
for key, value in dr.items():
    print(key, value)

# print(drecord1["parentId"])
# print(drecord1.get("parentId"))

# print(drecord1.popitem())

# print(drecord1)

# print(drecord1["pId"])
#table
# d = dict() # this creates an empty dictionary
# d = {} # this will empty dictionary

# the key in the dictionary must be an immutable object
# d = {"Ramana":[1, 2, 3, 4]} # here the list is provided as a key and String is provided as value
#print(d)

# d = {(1, 2, 3): "Ramana"}
# print(d)