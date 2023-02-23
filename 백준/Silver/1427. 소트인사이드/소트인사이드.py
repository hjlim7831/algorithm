import sys
input = sys.stdin.readline

number = list(map(int, input().rstrip()))
number.sort(reverse=True)
print("".join(map(str, number)))