import sys
input = sys.stdin.readline

document = input().rstrip()
word = input().rstrip()
ld, lw = len(document), len(word)

idx = 0
cnt = 0
while idx <= ld - lw + 1:
    if word == document[idx:idx+lw]:
        cnt += 1
        idx = idx + lw
    else:
        idx += 1

print(cnt)