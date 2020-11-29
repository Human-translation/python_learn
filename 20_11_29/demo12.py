class Turtle:
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = 'dazui'

    def climb(self): #self相当于c++的*this指针
        print('1')
    
    def run(self):
        print('2')
    
    def bite(self):
        print('3')
    
    def eat(self):
        print('4')

tt = Turtle()
print(tt.climb())

class MtList(list):
    pass
#继承


class Ball:
    def __init__(self,name): #__init__相当于c++中的构造函数
        self.name = name
    def kick(self):
        print("I am %s" % self.name)

b = Ball('tudou')
b.kick()


class Person:
    name = 'xiaojiayu'
    __age = '20' #双下滑线代表私有
    def GetAge(self):
        return self.__age

p = Person()
print(p.name)
print(p._Person__age) #双下划綫只是改了名称，是伪私有
print(p.GetAge())