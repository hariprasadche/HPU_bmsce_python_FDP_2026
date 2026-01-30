#definition: a dictionary is mutable, unordered, collection of keyvalue pairs

dict1 = {'name': "Hari", "age": 37, "city": "bengaluru"}
dict2 = {'name': "Prasad", "age": 35, "city": "Hyderabad"}
dict3 ={"name": ["google", "microsoft"],
        "ages": [45, 89],
        "cities": ["paris"]}

#printing dictionaries
print(dict1)
print(dict1["name"])
print(dict3)

#adding some values
dict1['job'] = "Trainer"
print(dict1)

#removing the elements from dict
#1) pop()
#2) popitem()
#3) del
#4) clear()

dict1.pop("age")
print(dict1)

#2) popitem() it will delete the latest key from the dictionary
dict1.popitem()
print(dict1)

#del key
del dict2["city"]
print(dict2)

#4) clear
dict3.clear()
print(dict3)

#dictionary fucntions
#1) keys
#2) values
#3) items()
#4) get(key)
#5) update()

mydict = {"name": "Hari", "age": 37, "city": "bengaluru"}

#1) keys()
key = mydict.keys()
print(key) #directly printing keys
print(type(key)) #trying to check the key type
for i in key:
    print(i) # iterate overs keys and printing them separately
print(list(key)) #print the keys as lists

#2) values
value = mydict.values()
print(value)
print(type(value))
for i in value:
    print(i)

#3) items()
item = mydict.items()
print(item)
print(type(item))
for i in item:
    print(i)

#4) get(key)
print(mydict.get("name"))

#5) update()
mydict.update({"city": "Hyderabad"})
print(mydict)