import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())

min_x, max_x = min(x, y), max(x, y)

if 2 * w >= s:
    ans = min_x * s
    left_d = max_x - min_x
    if w >= s:
        ans += left_d // 2 * 2 * s + left_d % 2 * w
    else:
        ans += left_d * w

else:
    ans = (max_x + min_x) * w

print(ans)