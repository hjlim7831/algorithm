import sys
N = int(sys.stdin.readline())
numl = [0 for i in range(N)]
for i in range(N):
    numl[i] = int(sys.stdin.readline())

mn = max(numl)+1

cou = [0 for i in range(mn)] # 자연수일 때만 가능한거겠지..
for i in range(N):
    cou[numl[i]] += 1

for i in range(1,mn):
    cou[i] = cou[i] + cou[i-1]

#print(cou)

numl2 = [0 for i in range(N)]

for i in range(N-1,-1, -1):

    numl2[cou[numl[i]]-1] = numl[i]
    cou[numl[i]] -= 1


print("\n".join(map(str,numl2)))



# 아니 근데 counting 정렬을 보니까 일반적인 정렬 방식보다 메모리가 많이 잡아먹힌다고 하던데
# 이 방식도 메모리 초과가 나는데 counting 정렬을 하는게 맞나..?
# python sort는 어떤 방식으로 하는거길래..흠 