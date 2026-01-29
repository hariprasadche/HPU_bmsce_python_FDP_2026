#write a program wheather the given number is prime or not
n = int(input("enter the number: "))
isPrime = True
if n < 2:
    isPrime = False
else:
    for i in range(2,n):
        if n % i == 0:
            print(f"{n} is not a prime number")
            isPrime = False
            break
print("prime" if isPrime else "not prime")
