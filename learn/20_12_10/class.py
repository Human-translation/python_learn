'''
class Person():
    name = "小甲鱼"

    def printf(self):
        print(self.name)

p = Person()
p.printf()


class Rectangle():
    length = 0
    weight = 0

    def set(self):
        print("请输入长和宽:")
        self.length = int(input("长:"))
        self.weight = int(input("宽:"))
    
    def get(self):
        print("长为 %d ,宽为 %d" % (self.length,self.weight))

    def getArea(self):
        print("面积为 %d " % self.length * self.weight)

rect = Rectangle()
rect.set()
rect.get()
rect.getArea()


class ticket():
    Day = ""
    Person = 0
    Son = 0

    def get(self):
        self.Day = input("打算哪天去游玩:")
        self.Person = int(input("有几个大人:"))
        self.Son = int(input("有几个小孩:"))

    def add(self):
        if self.Day == "周日" or self.Day == "周末":
            print("今天门票贵呢!")
            return 120 * self.Person + 60 * self.Son
        else:
            return 100 * self.Person + 50 * self.Son

P = ticket()
P.get()
print(P.add())

'''

import random as r

legal_x = [0, 10]
legal_y = [0, 10]

class Turtle:
    def __init__(self):
        # 初始体力
        self.power = 1000
        # 初始位置随机
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y        
        # 体力消耗
        self.power -= 1
        # 返回移动后的新位置
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 1000:
            self.power = 1000

class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
        
    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        # 返回移动后的新位置
        return (self.x, self.y)


print(issubclass(Turtle,Fish))