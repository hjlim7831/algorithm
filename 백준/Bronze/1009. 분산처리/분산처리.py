import sys
input = sys.stdin.readline

def pow(val, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        tmp = (pow(val, exp // 2)) % 10
        return (tmp * tmp) % 10
    else:
        tmp = pow(val, (exp - 1) // 2) % 10
        return (tmp * tmp * val) % 10

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    res = pow(a, b)
    if res == 0:
        res = 10
    print(res)