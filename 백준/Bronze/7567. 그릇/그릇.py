import sys
input = sys.stdin.readline

bowls = input().rstrip()

last = ""
ans = 0
for b in bowls:
    if last == b:
        ans += 5
    else:
        last = b
        ans += 10

print(ans)