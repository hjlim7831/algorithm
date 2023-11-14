import sys
input = sys.stdin.readline

S = input().rstrip()

st = S[0]
cnt = 1
for s in S[1:]:
    if st != s:
        cnt += 1
        st = s

print(cnt // 2)