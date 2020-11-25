num = {}
type(num)

num2 = {1,2,3,4,5}
type(num2)

num2 = {1,2,3,4,5,5,4,3,2,1}

set1 = set([1,2,3,4,5,5])

num1 = [1,2,3,4,5,5,3,1,0]
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)


num1 = list(set(num1))

'1' in num1
#可以使用in

num2.add(6)
num2.remove(5)

num3 = frozenset([1,2,3,4,5])
#不可修改