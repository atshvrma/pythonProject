class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        # print("Student Name:" + self.name)
        print(f"Marks: {self.marks}")

# Object creation
s1 = Student("Anjali", 88)
s1.display()

print("Another student")

s2 = Student("Rahul", 49)
s2.display()


s3 = Student()
s3.display()