f = open('F:\\learning.txt') #打开文件,默认为只读r，以w方式打开则会清空文件
str = f.read() #读取size个字符，若为负数则全部读取，同时文件指针移动
f.tell() #查看文件指针位置
f.seek(45,0) #修改文件指针位置，0为开头，1为当前，2为末尾
f.seek(0,1)
f.seek(0,2)
f.readline() #读一行

f.seek(0,0)
line = list(f)
for i in line:
    print(i)
#需要创建一个非常大的列表，效率低

f.seek(0,0)
for i in f:
    print(i)

f.write("nihao") #若指针处有值则覆盖，无值则添加

f.close()

f = open('F:\\learning.txt','w')
