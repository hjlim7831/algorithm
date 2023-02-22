import sys
input = sys.stdin.readline

N = int(input())

count_arr = [0 for _ in range(10001)]

for _ in range(N):
    count_arr[int(input())] += 1

for i in range(10001):
    for j in range(count_arr[i]):
        print(i)