#write a program to create student grading system with validity
#Take 5 subject marks input (total marks = 500)
#calculate percentage
#marks can only be entered between 1 to 100
#negative marks should be checked

a = int(input("Enter the marks of first subject: "))
b = int(input("Enter the marks of second subject: "))
c = int(input("Enter the marks of third subject: "))
d = int(input("Enter the marks of fourth subject: "))
e = int(input("Enter the marks of fifth subject: "))
sum = a + b + c + d + e
if 0 <= a <= 100:
    if 0 <= b <= 100:
        if 0 <= c <= 100:
            if 0 <= d <= 100:
                if 0 <= e <= 100:
                    percentage = (sum / 500)*100
                    if percentage >= 75:
                        print("student obtained A grade")
                    elif 75 > percentage >= 50:
                        print("student obtained B grade")
                    elif 50 > percentage >= 30:
                        print("student obtained C grade")
                    else:
                        print("Fail")
                else:
                    print("marks e are invalid")
            else:
                print("marks d are invalid")
        else:
            print("marks c are invalid")
    else:
        print("marks b are invalid")
else:
    print("marks a are invalid")





