class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to school.")

anna = Student("Anna", "MIT")
anna.marks.append(100)
print(anna.marks)
print(anna.avg())
Student.go_to_school()
