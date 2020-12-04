def fun1():
    str = input("请输入需要检查的密码组合:")

    num = len(str)
    judge1 = False
    judge2 = False
    judge3 = False

    while str.isspace() or num==0:
        print("你的输入为空")
        str = input("请重新输入:")
        num = len(str)

    for i in str:
        if '0'<i<'9':
            judge1 = True
        elif 'a'<i<'z' or 'A'<i<'Z':
            judge2 = True
        else:
            judge3 = True

    if num >= 16 and judge1+judge2+judge3 == 3:
        print("很好")
    elif num < 8 or judge1+judge2+judge3 == 1:
        print("您的密码安全评级定位：低")
        print("请按以下方式提升您的密码安全评级:")
        print("\t1.密码必须有数字、字母级特殊字符三种组合")
        print("\t2.密码只能由字母开头")
        print("\t3.密码长度不能低于16位")
    else:
        print("您的密码安全评级定位：中")
        print("请按以下方式提升您的密码安全评级:")
        print("\t1.密码必须有数字、字母级特殊字符三种组合")
        print("\t2.密码只能由字母开头")
        print("\t3.密码长度不能低于16位")

str = "asdfghjklasjklasjkl"
arr = 0
count = 0
while(arr != -1):
    arr = str.find("as",arr+1)
    print(str.find("as"))
    count += 1