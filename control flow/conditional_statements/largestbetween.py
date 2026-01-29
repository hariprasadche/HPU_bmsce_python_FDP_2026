#write a program to check the largest between three numbers

a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
if a>b and a>c:
    print("The number a is largest of all", a)
    print("The number b is largest of all", b)
else:
    print("The number c is largest of all", c)