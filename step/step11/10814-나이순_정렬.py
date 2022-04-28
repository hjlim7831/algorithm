# 카운팅 정렬로 시간 단축에 성공했다!! 근데 조금 더 익숙해질 필요가 있을 듯.. 아직 좀 헷갈린다.
# 학습의 결과인가 ㅋㅋ

import sys

N = int(sys.stdin.readline())
xage = [""]*N
xnam = [""]*N

xct = [0]*201

for i in range(N):
    age, nam = list(sys.stdin.readline().strip().split())
    xage[i], xnam[i] = int(age), nam
    xct[int(age)] += 1

for i in range(1,201):
    xct[i] += xct[i-1]

sxage, sxnam = [""]*N, [""]*N

for i in range(N-1, -1, -1):
    age = xage[i]
#    print(age)
    sxage[xct[age]-1] = age
    sxnam[xct[age]-1] = xnam[i]
    xct[age] -= 1


for i in range(N):
    print(sxage[i], sxnam[i])