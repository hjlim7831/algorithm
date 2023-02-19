import sys
input = sys.stdin.readline

chklist = [True for _ in range(31)]

for _ in range(28):
    num = int(input())
    chklist[num] = False

for i in range(1, 31):
    if chklist[i]:
        print(i)