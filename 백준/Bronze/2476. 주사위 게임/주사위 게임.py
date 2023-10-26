import sys
input = sys.stdin.readline

N = int(input())

ans = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    if a == b == c:
        tmp_ans = 10_000 + a * 1_000
    elif a == b:
        tmp_ans = 1_000 + a * 100
    elif b == c:
        tmp_ans = 1_000 + b * 100
    elif c == a:
        tmp_ans = 1_000 + c * 100
    else:
        tmp_ans = max(a, b, c) * 100

    ans = max(ans, tmp_ans)

print(ans)