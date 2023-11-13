import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))

    max_val = 0
    max_profit = 0
    for i in range(N-1, -1, -1):
        # 현재 주식을 사서 나중에 팔지 말지 결정
        if stock[i] < max_val:
            max_profit += max_val - stock[i]

        # 최댓값 갱신
        max_val = max(max_val, stock[i])
    print(max_profit)