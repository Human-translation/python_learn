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
    print('参数的长度是:',len(params),"nihao"+"shen")
    print('第二个参数是:',params[1])

test(1,2,3,4,5,6,78)