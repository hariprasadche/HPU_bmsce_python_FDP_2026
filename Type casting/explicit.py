#write a program in python to calculate the age of the user
name=input("Enter your name:")
birthday=int(input("Enter your birthyear:"))
print("type of birthday",type(birthday))
presentyear=int(input("Enter your presentyear:"))
print("type of presentyear",type(presentyear))
age=presentyear-birthday #type casting
print("your age is "+ str(age))
print(name + "-your age is "+ str(age))

#formatted strings way
print(f"{name} your age is {age}") #easiest way
print("{} your age is {} ".format(name,age))
