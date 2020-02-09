import pickle
class Everything:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(добавлен человек:{0})'.format(self.name))
    def tell(self):
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")
class Friend(Everything):
    def __init__(self,name,age,belive):
        Everything.__init__(self,name,age)
        self.belive= belive
        print('добавлен друг {0}'.format(self.name))
    def tell(self):
        Everything.tell(self)
        print('доверие:{0}'.format(self.belive))
class Bestfriend(Everything):
    def __init__(self,name,age,time):
        Everything.__init__(self,name,age)
        self.time=time
        print('добавлен лучший друг {0}'.format(self.name))
    def tell(self):
        Everything.tell(self)
        print('уже {0} лет'.format(self.time))
i=Bestfriend('jonh',14,6)
t=Friend('tanya',14,50)
members = [i, t]
private=['любит сладкое','геймер']
for member in members:
    member.tell()

print(type(i))



