class Robot:
    population = 0
    def __init__(self,name):
        '''инициализация'''

        self.name = name
        print('(Иициализация{0})'.format(self.name))
        Robot.population+=1
    def __del__(self):
        '''i died'''
        print('{0} died'.format(self.name))
        Robot.population -=1
        if Robot.population == 0:
            print('{0} was last'.format(self.name))
        else:
            print('осталось {0:d}'.format(Robot.population))
    def sayhi(self):
        '''приветствие'''
        print('приветствуем,меня зовут {0}'.format(self.name))
    def howmany():
        print('у нас {0:d}'.format(Robot.population))
    howmany=staticmethod(howmany)
droid1 = Robot('R2-D2')
droid1.sayhi()
Robot.howmany()
droid2 = Robot('C-3PO')
droid2.sayhi()
Robot.howmany()
print("\nЗдесь роботы могут проделать какую-то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2
Robot.howmany()