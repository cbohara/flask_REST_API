class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)

    @staticmethod
    def go_to_school():
        print("I'm going to school.")


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


anna = Student("Anna", "MIT")
anna.marks.append(100)
anna.marks.append(50)
print(anna.marks)
print(anna.avg())

friend = Student.friend(anna, "Steve")
print(friend.name)
print(friend.school)

Student.go_to_school()

charlie = WorkingStudent("Charlie", "UCSB", 10000, "Software Engineer")
print(charlie.name)
print(charlie.school)
print(charlie.salary)

dan = WorkingStudent("Dan", "UCSD", 20000, "Diva")
working_friend = WorkingStudent.friend(dan, "Alex", 500, "Carpenter")
print(working_friend.name)
print(working_friend.school)
print(working_friend.salary)
