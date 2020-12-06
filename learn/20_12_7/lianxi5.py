def fun1():
    str1 = "F:/python_code/"
    str2 = input("请输入文件名:")

    f = open(str1+str2,"w")

    arr = ""
    while 1:
        arr = input()
        if arr == ":w":
            break
        f.write(arr)
        f.write("\n")

    f.close()



def fun2():
    str0 = "F:/python_code/"
    str1 = input("请输入需要比较的头一个文件名:")
    str2 = input("请输入需要比较的另一个文件名:")

    f1 = open(str0+str1)
    f2 = open(str0+str2)

    count = 0
    list1 = []
    list2 = []

    for i in f1:
        list1.append(i)

    for i in f2:
        list2.append(i)

    length1 = len(list1)
    length2 = len(list2)

    i = 0
    while i<length1 and i<length2:
        if list1[i] != list2[i]:
            print("第 %d 行不一样" % (i+1))
            count += 1
        i += 1
    print("两个文件共有 %d 处不同" % count)
    f1.close()
    f2.close()



def fun3():
    str1 = "F:/python_code/"
    str2 = input("请输入要打开的文件名:")
    num = int(input("请输入需要显示该文件前几行"))

    i = 0
    f = open(str1+str2)
    print("文件 %s 的前 %d 行的内容如下:" % (str2,num))

    while i < num:
        print(f.readline())
        i += 1
    f.close()



def fun4():
    list1 = []
    list2 = []
    str1 = "F:/python_code/"
    str2 = input("请输入要打开的文件名:")
    num = input("请输入需要显示的行数【格式如 1:5】->")
    list1= num.split(':')

    f = open(str1+str2)
    #print("文件 %s 的前 %d 行的内容如下:" % (str2,num))

    for i in f:
        list2.append(i)

    if list1[0] == '' and list1[1] == '':
        print("\n文件 %s 全文的内容如下:" % str2)
        for i in list2:
            print(i)
    elif list1[0] == '':
        list1[1] = int(list1[1])
        print("\n文件 %s 从开始到第 %d 的内容如下:" % (str2,list1[1]))
        for i in range(list1[1]):
            print(list2[i])
    elif list1[1] == "":
        list1[0] = int(list1[0])-1
        print("\n文件 %s 从第 %d 到结尾的内容如下:" % (str2,list1[0]+1))
        for i in range(list1[0],len(list2)):
            print(list2[i])
    else:
        list1[0] = int(list1[0])-1
        list1[1] = int(list1[1])
        print("\n文件 %s 从第 %d 到第 %d 行的内容如下:" % (str2,list1[0]+1,list1[1]))
        for i in range(list1[0],list1[1]):
            print(list2[i])
    f.close()



def fun5():
    str1 = "F:/python_code/"
    str2 = input("请输入文件名:")
    arr1 = input("请输入需要替换的单词或字符:")
    arr2 = input("请输入新的单词或字符:")

    list1 = []


    f1 = open(str1+str2)
    f2 = open(str1+"456.txt","w")
    for i in f1:
        list1.append(i)

    j = 0

    while j<len(list1):
        if arr1 in list1[j]:
            list1[j] = list1[j].replace(arr1,arr2)
        j += 1

    for i in list1:
        f2.write(i)
    f1.close()
    f2.close()


fun4()