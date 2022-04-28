# sys.stdin.readline()을 애용합시다..

import sys

N = int(sys.stdin.readline())

num = [0]*N
m1 = 0
for i in range(N):
    num[i] = int(sys.stdin.readline())
    m1 += num[i]

m1 = m1/N

num.sort()
m2 = num[int((N-1)/2)]

m4 = num[N-1] - num[0]

minm = num[0]
count = [0]*(m4+1) # 카운팅 정렬
for i in range(N):
    ind = num[i] - minm
    count[ind] += 1
maxc = max(count) # 가장 개수가 많을 때, 그 숫자의 개수

mc = []

for i in range(m4+1):
    if count[i] == maxc:
        mc.append(i + minm) # mc: 최빈값인 수의 모음

if len(mc) == 1:
    m3 = mc[0]

else:
    m3 = mc[1]

print(int(f"{m1:.0f}"))
print(m2)
print(m3)
print(m4)

