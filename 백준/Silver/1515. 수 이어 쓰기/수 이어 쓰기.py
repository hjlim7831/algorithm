import sys
input = sys.stdin.readline

N = input().rstrip()

n = 1
idx = 0
while idx < len(N):
    target = str(n)
    for tidx in range(len(target)):
        if idx >= len(N):
            break
        if N[idx] == target[tidx]:
            idx += 1
    n += 1

print(n-1)