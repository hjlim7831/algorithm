import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
D = int(input())

t = A * 3600 + B * 60 + C + D
hr = (t // 3600) % 24
t = t % 3600
mi = t // 60
t = t % 60
se = t

print(hr, mi, se)