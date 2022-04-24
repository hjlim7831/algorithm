# 타 답안의 경우가 훨씬 빠름!! 참고하기

import time
def star(slis, n):
    if n == 1:
        return slis
    else:
        ls = len(slis)
        n2 = n//3
        for i in range(0, ls, n):
            for j in range(0, ls, n):
                for k in range(i+n2,i+n2*2):
                    slis[k][j+n2:j+n2*2] = [" "] * n2

        return star(slis,n2)


N = int(input())
start = time.time()
stlis = [["*"]*N for i in range(N)]
#print(stlis)
stlis = star(stlis, N)
for st in stlis:
    for j in st:
        print(j, end="")
    print("")
print(time.time() - start)