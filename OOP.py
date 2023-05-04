class Person:
    def __init__(self, person_name: str, dob, h: int = None):
        self.name = person_name   # instance variable
        self.dob = dob
        self.height = h

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_all(self):
        return f"Name: {self.name} , DOB : {self.dob} , Height: {self.height if self.height is not None else 'Invalid'}"


a_person = Person("Robin", "13/06/1994", 5.6)

print(a_person.get_name())
print(a_person.get_all())

a_person.set_name("Robin Kuri")
print(a_person.get_all())

print(a_person.dob)
# __variableName or __methodName are defined as private

b_person = Person("Robin", "13/06/1994")

print(b_person.get_all())


# Inheritance

class Student(Person):
    def __init__(self, person_name: str, dob, email: str, id: str):
        super().__init__(person_name, dob)
        self.id = id
        self.email = email
# function Override

    def get_all(self):
        return f"Name: {self.name} , DOB : {self.dob} , email : {self.email}"


student = Student("Robi", "13/11/1990", "robin@hahah.com", "sgquywbn")
print(student.get_all())
student.set_name("Robi Das")
print(student.get_all())


class PlainClass:
    pass


abc = PlainClass()
abc.age = 30
abc.name = "Endmd\n"
print(abc.name)
