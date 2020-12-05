'''
g = lambda x,y=3 : x * y
print(g(3))

temp = range(100)
print(list(filter(lambda x : x if x%3==0 else None,temp)))
print(list(map(lambda x:x*3,range(1,34))))

arr = [1,3,5,7,9]
brr = [2,4,6,8,10]
print(list(map(lambda x,y:[x,y],arr,brr)))
'''
def fun1():
    dict1 = {}

    print("|---欢迎进入通讯录系统---|")
    print("|---1: 查询联系人资料---|")
    print("|---2: 插入新的联系人---|")
    print("|---3: 删除已有联系人---|")
    print("|---4: 退出通讯录系统---|")
    num = 1
    while num != 4:
        num = int(input("请输入相关的指令代码:"))
        if num == 1:
            str = input("请输入联系人姓名:")
            if str in dict1:
                print(str," : ",dict1[str])
            else:
                print("|---没有该用户！！---|")
        elif num == 2:
            str = input("请输入联系人姓名:")
            telephone = input("请输入用户联系电话:")
            if str not in dict1:
                dict1[str] = telephone
            else:
                flag = int(input("该联系人已存在，是否修改(0/1)"))
                if flag:
                    dict1[str] = telephone
        elif num == 3:
            str = input("请输入联系人姓名:")
            if str in dict1:
                dict1.pop(str)
                print("|---用户已删除---|")
            else:
                print("|---您输入的联系人不存在！！---|")
        elif num == 4:
            print("|---感谢使用通讯录系统---|")
        else:
            print("|---输入错误，请重新输入---|")

def fun2():
    dict2 = {}
    count = 0
    print("|---新建用户:N/n---|")
    print("|---登录账号:E/e---|")
    print("|---退出程序:Q/q---|")

    while 1:
        num = input("请输入指令代码:")
        if num=='N' or num=='n':
            name = input("请输入用户名:")
            while name in dict2:
                name = input("此用户名已经被使用，请重新输入:")
            password = input("请输入密码:")
            dict2[name] = password
            print("注册成功！")
        elif num=='E' or num=='e':
            name = input("请输入用户名:")
            while name not in dict2:
                name = input("您输入的用户名不存在，请重新输入:")
                count += 1
                if count == 2:
                    print("失误过多，程序退出！")
                    return
            count = 0
            password = input("请输入密码:")
            while dict2[name] != password:
                password = input("您输入的密码不正确，请重新输入:")
                count += 1
                if count == 2:
                    print("失误过多，程序退出！")
                    return
            print("欢迎进入XXOO系统，请点击右上角的x结束程序！")
        elif num=='Q' or num=='q':
            print("程序退出")
            return 


f1 = open("F:\\python_code\\OpenMe.MP3")
f2 = open("F:\\python_code\\OpenMe.txt","w")

f2.write(f1.read())
f1.close()
f2.close()