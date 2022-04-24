"""
리스트 부분을 빼고, 직접 호출하는 식으로 하니 계산속도가 확실하게 느려졌다. 왜 그럴까..?
"""

import math
import time

def IsPrime(num):
    a = int(math.sqrt(num))
    if num == 1:
        return False
    else:
        for i in range(2, a+1):
            if num % i == 0: 
                return False
        return True

while True:
    n = int(input())
    start = time.time()
    if n == 0:
        break
    cnt = 0
    for i in range(n+1,n*2+1):
        if IsPrime(i):
            cnt += 1
    print(cnt)
    print("time: ",time.time() - start)