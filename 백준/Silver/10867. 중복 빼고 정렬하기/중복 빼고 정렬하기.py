import sys
input = sys.stdin.readline

N = int(input())
ans = list(set(map(int, input().split())))
ans.sort()

print(*ans)