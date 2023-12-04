import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ac_mileages = []

for _ in range(n):
    P, L = map(int, input().split())
    mileages = list(map(int, input().split()))
    if P < L:
        ac_mileages.append(1)
    else:
        mileages.sort(reverse=True)
        score = mileages[L-1]
        ac_mileages.append(score)

# print(ac_mileages)
ac_mileages.sort()

answer = 0
acc_score = 0
if ac_mileages[0] <= m:
    for idx, score in enumerate(ac_mileages):
        acc_score += score
        if acc_score > m:
            answer = idx
            break
    else:
        answer = n

print(answer)



