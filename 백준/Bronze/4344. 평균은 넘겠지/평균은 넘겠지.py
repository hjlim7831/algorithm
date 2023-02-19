import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    input_list = list(map(int, input().split()))
    score = input_list[1:]
    num = input_list[0]
    avg_score = sum(score) / num
    case = 0
    for sc in score:
        if avg_score < sc:
            case += 1
    print(f"{case / num * 100:.3f}%")