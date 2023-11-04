import sys
input = sys.stdin.readline

N = int(input())
main_word = input().rstrip()
words = [input().rstrip() for _ in range(N-1)]

mw_cnt = [0] * 26
for w in main_word:
    mw_cnt[ord(w) - ord("A")] += 1

ans = 0
for word in words:
    w_cnt = [0] * 26
    for w in word:
        w_cnt[ord(w) - ord("A")] += 1
    
    abs_sum = 0
    diff_sum = 0

    for i in range(26):
        abs_sum += abs(mw_cnt[i] - w_cnt[i])
        diff_sum += mw_cnt[i] - w_cnt[i]
    
    if abs_sum <= 1:
        ans += 1
    elif abs_sum == 2 and diff_sum == 0:
        ans += 1

print(ans)