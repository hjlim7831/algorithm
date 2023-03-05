import sys
input = sys.stdin.readline

eq = input().rstrip()

ans = 0
tmp = 0
flag = False
for s in eq:
    if s.isdigit():
        tmp = tmp * 10
        tmp = tmp + int(s)
    else:
        if flag:
            ans -= tmp
            tmp = 0
        else:
            ans += tmp
            tmp = 0
        if s == "-":
            flag = True

if flag:
    ans -= tmp
else:
    ans += tmp

print(ans)