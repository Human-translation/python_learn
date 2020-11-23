brand = ['a','b','c','d']
slogan = ['1','2','3','4']

print('a',slogan[brand.index('a')])

dict1 = {'a':'1','b':'2','c':'3','d':'4'}
print('a',dict1['a'])

dict2 = dict((('F',70),('i',105)))
print(dict2)

dict3 = dict(huahua='1',hanbao='2')
print(dict3)

dict3['huahua'] = '3'
print(dict3)

dict4 = {}
dict4.fromkeys((1,2,3))
print(dict4)
dict4.fromkeys((1,2,3),'Number')
print(dict4)
#fromkeys可以给每个键赋值

dict5 = {}
dict5 = dict5.fromkeys(range(32),'hao')
#修改原先的字典变为新
for i in dict5.keys():
    print(i)
#keys()输出所有key值
for i in dict5.values():
    print(i)
#values()输出所有value值
for i in dict5.items():
    print(i)
#items()输出所有键值对

dict5.get(32)
#get()访问没有的键值时则返回空，不报错
dict5.get(32,"meiyou")
#有则返回正常值，没有则返回括号里面的值
dict5.clear()
#clear()清空

dict6 = {1:"2"}
dict6.setdefault(2,"3")
dict6.setdefault(5)
#添加新键值对
print(dict6)

a = {1:"1",2:"2",3:'3',4:'4'}
b = a.copy()
#浅拷贝
c = a
#赋值，修改a，c也会变
print(id(a),id(b),id(c))

a.pop(2)
#删除给定的
print(a)
b.popitem()
#删除最后一个
print(b)

c = {1:"1",2:"2",3:'3',4:'4'}
b = {1:"10",5:"5"}
c.update(b)
#用b更新
print(c)

