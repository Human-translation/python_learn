def printf():
    arr = int(input())

    i = arr
    while i > 0:
        print(' ' * (i-1),'*' * i)
        i -= 1

def judge(num):
    if (num%4 ==0 and num%100 != 0) or num%400 ==0:
        return 1
    return 0

print(judge(2019))