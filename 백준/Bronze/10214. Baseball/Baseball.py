import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sum_y, sum_k = 0, 0
    for _ in range(9):
        Y, K = map(int, input().split())
        sum_y += Y
        sum_k += K
    if sum_y > sum_k :
        print("Yonsei")
    elif sum_y < sum_k:
        print("Korea")
    else:
        print("Draw")