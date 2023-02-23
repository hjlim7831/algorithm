import sys
input = sys.stdin.readline

judges = []

N = int(input())
for _ in range(N):
    age, name = input().rstrip().split()
    judges.append((int(age), name))

judges.sort(key=lambda x: x[0])

for judge in judges:
    print(*judge)