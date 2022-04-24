import time
import math # 이건 생각보다 큰 영향을 안 미치는 듯
def isprime(n):
    prime = [i for i in range(2*n+1)]
    prime[:2] = [-1, -1]
    k = 0
    i = 2
    while k <= math.sqrt(2*n):
        if prime[k] == -1:
            k += 1
            continue
        while True:
            if prime[k] * i > 2*n:
                k += 1
                i = 2
                break
            prime[prime[k] * i] = -1
            i += 1
    pr = [i for i in prime[n+1:] if i != -1]
    return len(pr)

while True:
    n = int(input())
    start = time.time()
    if n == 0:
        break
    print(isprime(n))
    print("time: ",time.time() - start)

