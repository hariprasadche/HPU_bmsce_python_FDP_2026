#definition: a tuple is ordered, immutable collection of items
#properties
#ordered
#immutable
#allows duplicates

mytuple = (1,2,3,4,5,6,7,8,9, 9, 2.8, "HARI", "Department of chemical engineering")
print(mytuple)
anothertuple = tuple(range(2, 101, 2))
print(anothertuple)

#access the elements from tuple
print(mytuple[4])
print(mytuple[10:12])

#operations on tuples
#1) concatination of 2 tuples using + operator
tuple1 = (1,2,3)
tuple2 = (4,5,6)
result = tuple1 + tuple2
print(result)

#2) repitition of tuples
originaltuple = (1,2,3)
repeatedtuple = originaltuple * 3
print(repeatedtuple)

#3) membership of an element inside the tuple
sampletuple = (1,2,3,4,5,6,7,8,9)
print(3 in sampletuple)
print(20 in sampletuple)
print(3 not in sampletuple)
#length of a tuple
length = len(sampletuple)
print(length)

#index() find out the index of an element in a tuple

index = mytuple.index("HARI")
print(index)
#count() counting the number of occurances of an element inside the tuple
count = mytuple.count(9)
print(count)

#note: there are only 2 inbuilt fucntions in tuple - index and count
#why? - because tuples are immutable, they cannot be modofied
#so we have limited options in tuple
#once tuple is created you cannot change anything in it
