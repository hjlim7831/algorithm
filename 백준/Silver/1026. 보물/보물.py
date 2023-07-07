import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))
A.sort()
B.sort(reverse=True)
ans = 0
for a, b in zip(A, B):
    ans += a * b
print(ans)
