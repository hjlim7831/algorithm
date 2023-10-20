import sys
input = sys.stdin.readline

A = input().rstrip()
op = input().rstrip()
B = input().rstrip()

la, lb = len(A), len(B)

if op == "*":
    ans = "1"+"0" * (la + lb - 2)
else:
    ml, Ml = min(la, lb), max(la, lb)
    if ml != Ml:
        ans = "1" + "0" * (Ml - ml - 1) + "1" + "0" * (ml-1)
    else:
        ans = "2" + "0" * (ml - 1)
print(ans)