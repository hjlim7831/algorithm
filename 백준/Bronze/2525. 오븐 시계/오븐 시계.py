import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())

total = A * 60 + B + C

min = total % 60
hr = (total // 60) % 24

print(hr, min)