import sys
input = sys.stdin.readline

cnt = [0 for _ in range(26)]
word = input().rstrip().upper()

for w in word:
    cnt[ord(w) - ord("A")] += 1

max_cnt = max(cnt)
mul = 0
idx = -1
for i in range(len(cnt)):
    if max_cnt == cnt[i]:
        idx = i
        mul += 1

if (mul == 1):
    print(chr(idx + ord("A")))
else:
    print("?")