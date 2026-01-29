def fibi(n):
    if n==0 or n==1:
        return n
    return fibi(n-1) + fibi(n-2)
n = int(input("Enter a number: "))
for i in range(n):
    print(fibi(i), end=" ")
