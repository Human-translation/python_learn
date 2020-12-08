import easygui as g
import sys
import random
import os

def fun():
    while 1:
        g.msgbox("嗨，欢迎进入第一个界面小游戏^_^","开始")

        msg ="请问你希望在鱼C工作室学习到什么知识呢？"
        title = "小游戏互动"
        choices = ["谈恋爱", "编程", "OOXX", "琴棋书画"]
            
        choice = g.choicebox(msg, title, choices)

            # 注意，msgbox的参数是一个字符串
            # 如果用户选择Cancel，该函数返回None
        g.msgbox("你的选择是: " + str(choice), "结果")

        msg = "你希望重新开始小游戏吗？"
        title = "请选择"

            # 弹出一个Continue/Cancel对话框
        if g.ccbox(msg, title):
            pass            # 如果用户选择Continue
        else:
            sys.exit(0)     # 如果用户选择Cancel

'''
g.msgbox("hello world","你好世界")
g.msgbox("hello world","你好世界","加油")

if g.ccbox():
    pass
else:
    sys.sxit(0)

if g.ccbox(msg='Shall I continue?', title=' ', choices=('C[o]ntinue', 'C[a]ncel'), image=None, default_choice='C[o]ntinue', cancel_choice='C[a]ncel'):
    pass
else:
    sys.sxit(0)
#可以敲o 或者 a选择

ynbox()
#与ccbox()相同，只是参数为是与否，而ccbox为继续与退出

list1 = ["草莓","香蕉","苹果"]
g.buttonbox("你会选择什么","我是标题",list1)
g.buttonbox("你会选择什么","我是标题",list1,imag="F:/python_code/33.png")

g.indexbox()
g.boolbox()

choices = ['愿意', '不愿意', '有钱的时候就愿意']
reply = g.choicebox('你愿意购买资源打包支持小甲鱼吗？', choices = choices)
#有选项但只能选一个

g.multchoicebox()
#有选项可以多选

g.enterbox()
#用户输入字符串，返回
g.integerbox(msg='', title=' ', default=None, lowerbound=0, upperbound=99, image=None, root=None)
#用户输入限定内的整数超过则重新输入
g.multenterbox()
#输入多个信息，姓名电话之类
g.passwordbox()
#输入密码可用
g.multpasswordbox()
#多个输入最后一个框为*******

g.textbox()
g.codebox()
#两种输入文本方式

g.diropenbox()
g.fileopenbox()
g.filesavebox()
#三种选择目录的方法
'''



def fun2():
    count = 0
    number = random.randint(0,100)
    num = int(g.enterbox("来猜猜我在想什么数(1~100):","数字小游戏"))
    while number != num:
        if num > number:
            num = int(g.enterbox("你猜的谁有点大了诶，再猜一次吧","数字小游戏"))
        elif num < number:
            num = int(g.enterbox("你猜的谁有点小了诶，再猜一次吧","数字小游戏"))
        count += 1
    g.msgbox("猜中了恭喜,您花了 %d 次猜中答案" % count,"数字小游戏",image="F:/python_code/33.png")


def fun3():
    msg = "请填写以下联系方式"
    title = "账号中心"
    fieldNames = [" *用户名", " *真实姓名", "  固定电话", " *手机号码", "  QQ", " *E-mail"]
    fieldValues = []
    fieldValues = g.multenterbox(msg, title, fieldNames)



list1 = {".cpp":0,".py":0}


def fun4():
    
    str = g.diropenbox()
    str += '/'
    bianli(str)
    
    g.textbox(list1)

def bianli(str):
    
    arr = os.listdir(str)
    for i in arr:
        if os.path.isdir(str+i+"/") and ".vscode" not in i:
            bianli(str+i+"/")
        elif  ".hpp" in i:
            f = open(str+i,encoding='utf-8')
            list2 = f.read()
            f.close()
            count = list2.count("\n")
            list1[".cpp"] = list1[".cpp"] + count
        elif '.cpp' in i:
            f = open(str+i,encoding='utf-8')
            list2 = f.read()
            f.close()
            count = list2.count("\n")
            list1[".cpp"] = list1[".cpp"] + count
        elif '.py' in i:
            f = open(str+i,encoding='utf-8')
            list2 = f.read()
            f.close()
            count = list2.count("\n")
            list1[".py"] = list1[".py"] + count




fun4()








