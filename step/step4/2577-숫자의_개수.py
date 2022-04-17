A = int(input())
B = int(input())
C = int(input())
ABC = str(A*B*C)
c = [0 for i in range(10)]
for i in range(len(ABC)):
    ii = int(ABC[i])
    c[ii] += 1
for i in range(10):
    print(c[i])