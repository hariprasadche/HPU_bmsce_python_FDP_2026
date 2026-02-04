class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printdetails(self):
        print(f"student name: {self.name}, age: {self.age}")

s1 = Student("John", 25)
s2 = Student("Mike", 30)
s3 = Student("Hari", 35)
s1.printdetails()
s2.printdetails()
s3.printdetails()