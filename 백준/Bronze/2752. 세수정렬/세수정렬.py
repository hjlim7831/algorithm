import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
numbers.sort()
print(*numbers)