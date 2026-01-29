#write a python program to calculate the simple interest
principal_amount=float(input("please enter your principal amount:"))
interest_rate = float(input("please enter your interest rate:"))
time_period = int(input("please enter your time_period:"))
print("principal amount is", type(principal_amount))
print("interest rate is", type(interest_rate))
print("time_period is", type(time_period))
simple_interest = principal_amount * time_period*interest_rate/100
print("simple interest is", float(simple_interest))
