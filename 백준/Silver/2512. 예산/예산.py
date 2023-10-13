import sys
input = sys.stdin.readline

N = int(input())
requests = list(map(int, input().split()))
requests.sort()
M = int(input())
answer = 0
def binary(st, ed):
    # print(st, ed)
    if st > ed:
        return
    global answer
    m = (st + ed) // 2
    tot = 0
    for idx, val in enumerate(requests):
        if val >= m:
            tot += (N - idx) * m
            break
        else:
            tot += val
    # print("tot:", tot)
    if tot > M:
        binary(st, m-1)
    else:
        tmp_ans = min(requests[-1], m)
        # print(tmp_ans)
        answer = max(answer, tmp_ans)
        binary(m+1, ed)

binary(0, 100_000)

print(answer)