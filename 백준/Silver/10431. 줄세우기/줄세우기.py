import sys
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    cases = list(map(int, input().split()))
    T = cases[0]
    heights = cases[1:]
    cnt = 0
    s_list = []
    for h in heights:
        s_list.append(h)
        for i in range(-1, -len(s_list), -1):
            if s_list[i] < s_list[i-1]:
                s_list[i], s_list[i-1] = s_list[i-1], s_list[i]
                cnt += 1
            else:
                break
    print(T, cnt)
