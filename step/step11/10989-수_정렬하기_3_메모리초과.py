import sys
N = int(sys.stdin.readline())
numl = [0 for i in range(N)]
for i in range(N):
    numl[i] = int(sys.stdin.readline())
numl.sort()
print("\n".join(map(str,numl)))

# 아니 근데 counting 정렬을 보니까 일반적인 정렬 방식보다 메모리가 많이 잡아먹힌다고 하던데
# 이 방식도 메모리 초과가 나는데 counting 정렬을 하는게 맞나..?
# python sort는 어떤 방식으로 하는거길래..흠 