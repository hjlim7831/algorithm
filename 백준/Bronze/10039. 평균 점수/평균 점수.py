import sys
input = sys.stdin.readline

scores = [max(int(input()), 40) for _ in range(5)]

print(sum(scores) // 5)