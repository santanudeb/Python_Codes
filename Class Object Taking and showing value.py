class human():
    name = ''
    age = 0

    def get_name (self):
        print("Enter name")
        self.name=input()

    def get_age (self):
        print("Enter age")
        self.age=input()

    def put_name (self):
        print("Name is ", self.name)

    def put_age (self):
        print("Age is ", self.age)


person1 = human()
person1.get_name()
person1.get_age()
person1.put_name()
person1.put_age()