# 에라토스테네스의 체를 사용하는 쪽이 훨씬 짧게 걸리는 듯 하다.

import time
def isprime(n):
    c = 0
    for i in range(n+1, 2*n+1):
        if i == 2:
            c += 1
            continue
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                break
#        if j == int((2*n)**0.5):
        else:
            c += 1
    return c

while True:
    n = int(input())
    start = time.time()
    if n == 0:
        break
    print(isprime(n))
    print("time: ",time.time() - start)

