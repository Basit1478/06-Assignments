class Student:
    def __init__(self, name, marks):
        self.name = name          # 'self.name' is an instance variable
        self.marks = marks        # 'self.marks' is an instance variable

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")


# Example usage
student1 = Student("Abyan", 92)
student2 = Student("Fatima", 88)

student1.display()
print("---")
student2.display()
