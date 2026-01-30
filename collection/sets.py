#definition: A set is unordered collection of uinque elements
#properties
#unordered #order of hashing is considered
#mutbale
#does not allow duplicates

myset = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(myset)

#adding elements
myset.add(10)
print(myset)

#remove element
myset.remove(8) #remove will give error is element is not available in set
print(myset)

#discard
myset.discard(7) #discard() will not give any error message
print(myset)

myset.pop()
print(myset)

myset = {1,1,2}


print(myset)
set1 = {1,2,3}
set2 = {3,5,6}
union = set1 | set2
print(union)

intersection = set1 & set2
print(intersection)

difference = set1 - set2
print(difference)

difference = set2 - set1
print(difference)
