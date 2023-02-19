import sys
input = sys.stdin.readline

max_num = 0
idx = -1
for i in range(1, 10):
    num = int(input())
    if max_num < num:
        idx = i
        max_num = num
print(max_num)
print(idx)