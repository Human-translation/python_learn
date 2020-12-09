import os

def fun1():
    files = os.listdir(os.curdir)
    print(files)

    arr = {}
    count = 1
    wenjian = 0

    for i in files:
        if "." in i:
            (name,cizhui) = i.split(".",1)
            if cizhui in arr:
                arr[cizhui] += 1
            else:
                arr[cizhui] = 1
        else:
            wenjian += 1

    for i in arr.items():
        (name,num) = i
        print("该文件夹下共有类型为【.%s】的文件 %d 个" % (name,num))
    print("该文件夹下共有类型为【文件夹】的文件 %d 个" % wenjian)
#统计文件类型文件数

def fun2():
    str0 = "F:/python_code/"
    str1 = os.listdir(os.curdir)
    for i in str1:
        print(i,"【",os.path.getsize(str0+i),"】")
#计算文佳大小

def fun3(str0):
    os.chdir(str0)
    str1 = os.listdir(str0)
    for i in str1:
        if not os.path.isdir(str0+i):
            (name,cizhui) = i.split(".",1)
            if cizhui == 'mp4':
                print(str0,i)
        else:
            fun3(str0+i+'/')
            os.chdir(os.pardir)
            
fun3("F:/BaiduNetdiskDownload/test/")