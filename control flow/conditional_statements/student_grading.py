#write a program to create student grading system
#Take 5 subject marks input (total marks = 500)
#calculate percentage
#decide the grade of that student; above75% = A
a = int(input("Enter the marks of first subject: "))
b = int(input("Enter the marks of second subject: "))
c = int(input("Enter the marks of third subject: "))
d = int(input("Enter the marks of fourth subject: "))
e = int(input("Enter the marks of fifth subject: "))
sum = a + b + c + d + e
print("The sum is", sum)
percentage = (sum / 500)*100
print("The percentage is", percentage)
if percentage >= 75:
    print("student obtained A grade")
elif 75 > percentage >= 50:
    print("student obtained B grade")
elif 50 > percentage >= 30:
    print("student obtained C grade")
else:
    print("student obtained D grade")

