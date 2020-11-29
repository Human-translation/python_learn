A = [3,6,2,3]
A.sort()
size = int(len(A))
num1 = A[size-1]
num2 = A[size-2]
num3 = A[size-3]
while (size-3) >= 0:
    num1 = A[size-1]
    num2 = A[size-2]
    num3 = A[size-3]
    if num1 + num2 <= num3:
        size -= 1;
        continue
    elif num2 + num3 <= num1:
        size -= 1;
        continue
    elif num1 + num3 <= num2:
        size -= 1;
        continue
    else:
        print( num1+num2+num3)
    
