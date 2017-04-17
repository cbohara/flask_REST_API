class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name):
        return cls(friend_name, origin.school)

    @staticmethod
    def go_to_school():
        print("I'm going to school.")


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


anna = Student("Anna", "MIT")
anna.marks.append(100)
anna.marks.append(50)
print(anna.marks)
print(anna.avg())

friend = Student.friend(anna, "Steve")
print(friend.name)
print(friend.school)

Student.go_to_school()

charlie = WorkingStudent("Charlie", "UCSB", 10000)
print(charlie.name)
print(charlie.school)
print(charlie.salary)

dan = WorkingStudent("Dan", "UCSD", 20000)
working_friend = WorkingStudent.friend(dan, "Alex")
print(working_friend.name)
print(working_friend.school)
print(working_friend.salary)
