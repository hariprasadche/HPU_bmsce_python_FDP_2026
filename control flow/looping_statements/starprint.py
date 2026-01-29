size = int(input("enter the size of your number: "))
for i in range(size):
    for space in range(size-i-1):
        print(" ",end="")
    for star in range(2*i+1):
        print("*",end="")
    print()
for i in range(size-2, -1, -1):
    for space in range(size-i-1):
        print(" ",end="")
    for star in range(2*i+1):
        print("+",end="")
    print()