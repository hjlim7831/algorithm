"""
이 쪽이 확실히 훨씬 계산 속도가 빠르다. 왜일까..?
미리 소수를 구해놓고, 구한 소수들 중에서 값을 호출하는 것이 왜 더 시간이 짧게 걸릴까?
이 경우, 여러 개의 test case를 적용하는 것이니 그 면에서는 분명 미리 구하는 것이 더 효율적이지만.. 단순히 한 케이스에 대해서만 비교해봐도 훨씬 짧게 걸린다.
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

st = time.time()
Num_list = list(range(2,246912))
Sort_list = []
for i in Num_list:
    if IsPrime(i):
         Sort_list.append(i)
print("list time: ",time.time() - st)
# 응..? 이게 훨씬 오래 걸리는데..?  왜 시간이 이렇게 되는거지?
# 무언가가 호출되기 전까지 리스트는 계산을 안하는건가..?
# 근데 결과를 내려면 일단 리스트를 계산해야될텐데.. 뭐지?
# input이 들어간 이후에 얼마나 걸리는지만 계산해서 그런가?

while True:
    n = int(input())
    start = time.time()
    if n == 0:
        break
    cnt = 0
    for i in Sort_list:
        if n < i <= n*2:
            cnt += 1
    print(cnt)
    print("time: ",time.time() - start)