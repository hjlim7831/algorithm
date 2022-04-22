import sys

A, B = sys.stdin.readline().split()

la, lb = len(A), len(B)
mab = max(la,lb)

if mab - la == 0:
    B = '0'*(mab - lb) + B
else:
    A = '0'*(mab - la) + A

result = ''
tenth = 0
for i in range(mab):
    ind = mab - i -1
    a, b = int(A[ind]), int(B[ind])
    result = str((a+b+tenth)%10) + result
    tenth = (a+b+tenth)//10

if tenth == 1:
    result = '1'+result

print(result)