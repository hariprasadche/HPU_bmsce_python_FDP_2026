class Student:
    """
    Represents a student using Object-Oriented Programming principles.
    """
    def __init__(self, name, age):
        """
        Initializes the student object with a name, age, and an empty list of grades.
        The __init__ method acts as a constructor in Python.
        """
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        """
        Adds a new grade to the student's list of grades.
        """
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Added grade {grade} for {self.name}.")
        else:
            print("Invalid grade. Grade must be between 0 and 100.")

    def calculate_average_grade(self):
        """
        Calculates and returns the average grade of the student.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """
        Displays the student's name, age, grades, and average grade.
        """
        average = self.calculate_average_grade()
        print(f"\n--- Student Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {average:.2f}") # Formats average to two decimal places
        print(f"---------------------------")

# --- Example Usage ---

# 1. Create instances (objects) of the Student class.
student1 = Student("Alice", 18)
student2 = Student("Bob", 17)

# 2. Add grades to the students using the methods.
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(92)

student2.add_grade(75)
student2.add_grade(80)
student2.add_grade(78)

# 3. Display the information for each student.
student1.display_info()
student2.display_info()