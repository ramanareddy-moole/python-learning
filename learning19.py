#set
# will maintain unique values only

unique_set = set([1, 2, 3, 4, 5, 5, 2, 1])

print(unique_set)

unique_set = {"IronMan", "SuperMan", "SpiderMan", "CaptainAmerica", "IronMan"}

set1 = {1, 2, 3, 4, 5}
set2 = {1, 5, 7, 9, 9}

set1.add(5)
set1.add(87)
print(set1.union(set2))

#print(set1[1])

#print(set1[0:3])
print(unique_set)

#union, intersection, sysmmetric_difference and normal difference
set3 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}
print(set3.union(set4)) # returns the elements in both the sets but removes the duplicates

print(set3.intersection(set4)) # this should return only the common elements in both the sets

print(set3.symmetric_difference(set4)) # this will return all the elements except the common elements

print(set3.difference(set4))

print(set4.difference(set3))