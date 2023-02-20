import sys
input = sys.stdin.readline

N = int(input())

ans = "long " * (N // 4) + "int"
print(ans)