mix = [1,2]
mix.append('huahua')
mix.extend(['niu','bi'])
mix.insert(0,'3')
mix.count(1)
mix.index(2,0,5) #第一个数在哪出现
mix.reverse()
print(mix)

num = mix[:]
print(num)

mix.remove(1)
del mix[0]
mix.pop()
mix.pop(1)
print(mix)

mix = [7,6,4,8,1,9,2]
mix.sort()
print(mix)

#元祖
temp = (1,)
temp = 1,
temp = ('h','e','l','o')
temp = temp[:3] + ('?',) + temp[3:]
print(temp)

num = {5,4,3,2,1}
num2 = [5,4,3,2,1]
max(num)
min(num)
len(num)
list(num)
tuple(num)
sum(num)
sum(num,20)
sorted(num)
reversed(num2)
list(reversed(num2))
enumerate(num2)
print(list(enumerate(num2))) #输出序号
#zip(a,b) #合并两个元祖 