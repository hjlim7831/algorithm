def d(n:int):
    ans = n
    for dig in str(n):
        ans += int(dig)
    return ans

# rng = 100
rng = 10_000

ans_list = [True for _ in range(rng + 1)]

for idx in range(1, rng + 1):
    next_idx = d(idx)
    if next_idx <= rng:
        ans_list[next_idx] = False

for idx in range(1, rng + 1):
    if (ans_list[idx]):
        print(idx)