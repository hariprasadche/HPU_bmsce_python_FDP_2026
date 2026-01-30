#definition - A list is a ordered, mutable collection of items

# Properties
#Ordered
#Mutable
#Allow duplicates

mylists = [1,2,3,4,5,6,7,8,9] #syntax using []
anotherlists = list(range(2, 101, 2))

#operations on lists
# access elements from mylists

print(mylists[3])
print(f"on 3rd index: {mylists[3]}")
print(f"on 2nd index: {anotherlists[2]}")
print(mylists[2:4])
print(anotherlists[10:25])
print(f"on the last index: {anotherlists[-1]}")

#2) modifying the elements
#because the lists are mutable we can modify the lists
mylists[3] = 50
print(mylists)


#3) printing the lists
#2 ways of printing the lists or any collection in python


#1st way
print(mylists)


#2nd way
for i in mylists:
    print(i, end=" ")
print()


#4) adding an elements to a list
#append() it will add the elements at the last of the list
mylists.append(100)
print(mylists)
for i in range(10, 20):
    mylists.append(i)
print(mylists)


#insert() it will insert the element at a particular position
mylists.insert(6, 100)
print(mylists)
mylists.insert(7, "hari")
print(mylists)


#5)removing the elements from lists
mylists.remove(15)
print(mylists)


#pop() removes always last element
mylists.pop()
print(mylists)
del mylists [5]
print(mylists)


#6) other functions
#print(len(mylists))
mylists.sort(reverse=True)
print(mylists)
print()
mylists.reverse()
print(mylists)
mylists.remove(5)
print(mylists)

del mylists["hari"]
print(mylists)





