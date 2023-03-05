class student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def show_student(self):
        print("name", self.name)
        print("age", self.age)
        print("branch", self.branch)

student1 = student("Zack", 15, "Science")

student1.show_student()
