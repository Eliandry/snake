class Schoolmember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(создан member: {0})'.format(self.name))
    def tell(self):
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")
class Teacher(Schoolmember):
    def __init__(self,name,age,salary):
        Schoolmember.__init__(self,name,age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))
    def tell(self):
        Schoolmember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))
class Student(Schoolmember):
    def __init__(self, name, age, marks):
        Schoolmember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))
    def tell(self):
        Schoolmember.tell(self)
        print('оценки {0:d}'.format(self.marks))
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
members = [t, s]
for member in members:
    member.tell()