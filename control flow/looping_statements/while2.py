def add(num1,num2):
    total = num1+num2
    return total
def sub(num1,num2):
    total = num1-num2
    return total
def mul(num1,num2):
    total = num1-num2
    return total
def div(num1,num2):
    total = num1/num2
    return total

while True:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number:"))
    operator = int(input("Enter a operation: \n1. add\n2. sub\n3. mul\n4. div"))
    match operator:
        case 1:
            print(f"{num1} + {num2} = {add(num1,num2)}")
        case 2:
            print(f"{num1} - {num2} = {sub(num1,num2)}")
        case 3:cm
            print(f"{num1} * {num2} = {mul(num1,num2)}")
        case 4:
            print(f"{num1} / {num2} = {div(num1,num2)}")
        case 5:
            print("Invalid operation")
            break
        case _:
            print("Bye")



