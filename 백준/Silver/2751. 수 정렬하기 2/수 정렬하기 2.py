import sys
N = int(sys.stdin.readline())
numl = [0 for i in range(N)]
for i in range(N):
    numl[i] = int(sys.stdin.readline())
numl.sort()
print("\n".join(map(str,numl)))