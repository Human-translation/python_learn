def MyFirstFunction(name):
    'hello' #函数文档
    print('this'+name+'good')

MyFirstFunction('lixiangyu')

print(MyFirstFunction.__doc__)
#__doc__

def Sum(numa,numb):
    print(numa + ' + ' + numb)

Sum(numb='1',numa='2') #函数可以反着赋值

def test(*params):
    print('参数的长度是:',len(params),"nihao")
    print('第二个参数是:',params[1])

test(1,2,3,4,5,6,78)

def discounts(price,rate):
    final_price = price * rate
    old_price = 50 #在函数内修改全局变量则会创建同名变量，修改并不影响函数外全局变量
    print(old_price)
    return final_price

old_price = 100
rate = 0.8
new_price = discounts(old_price,rate)
print(old_price)


def fun1():
    print('fun1()正在被调用')
    def fun2():
        print('fun2()正在被调用')
    fun2()
    
fun1()

def FunX(x):
    def FunY(y):
        return x * y
    return FunY
print(FunX(8)(5)) #闭包



#def Fun1():
#    x = 5
#    def Fun2():
#        x *= x
#        return x
#    return Fun2

#print(Fun1())

# global 是定义为全局变量的
# nonlocal是定义函数内部变量的

lambda y : 2 * y + 1
g = lambda y : 2 * y + 1
print(g(6))

lambda y,z : y+z
g = lambda y,z : y+z
print(g(6,7))

filter(None,[1,0,False,True])
#返回非0数

def odd(x):
    return x%2

temp = range(10)
show = filter(odd,temp)
filter(lambda x : x%2,range(10))
print(list(filter(lambda x : x%2,range(10))))

print(list(map(lambda x : x*2,range(10))))