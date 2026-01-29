#write a program on fibonacci series using loops and recursion
n = int(input("enter the number"))
n1 = 0
n2 = 1
sum = 0
print(n1, n2, end=" ")
for i in range(2, n):
    sum = n1+n2
    n1 = n2
    n2 = sum
    print(sum, end=" ")
    

