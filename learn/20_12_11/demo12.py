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


class Parent:
    def hello(self):
        print('正在调用父类的方法')
    
class Child(Parent):
    def hello(self):
        print('正在调用子类的方法')

p = Parent()
p.hello()
c = Child()
c.hello()



import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x = -1
        print('位置为:',self.x,self.y)
    
class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        #Fish.__init__(self) 这重写了父类的构造函数，需要重新调用
        super().__init__() #自动调用父类构造函数
        self.hungry = True
    
    def eat(self):
        if self.hungry:
            print("吃货的梦想")
            self.hungry = False
        else:
            print("饱了")


class Base1:
    def foo1(self):
        print("foo1 , base1")

class Base2:
    def foo2(self):
        print("foo2 , base2")

class C(Base1,Base2):
    x = 1

print(issubclass(C,Base1))
#判断C是否是Base1的子类

b = C()
print(isinstance(b,C))
print(isinstance(b,Base2))
#判断b是不是C的实体
#父类也返回true

print(hasattr(b,'x'))
#判断x是否是b的类成员变量
print(getattr(b,'x'))
print(getattr(b,'y',"没找到诶!"))
#找到就返回值，找不到就返回输入的可选项，没有就报错

setattr(b,"y",3)
#添加该成员变量
delattr(b,"y")
#删除成员变量