import sys
input = sys.stdin.readline

S = list(input().rstrip())
cnt0 = S.count("0")
cnt1 = S.count("1")

rcnt = 0
for i in range(len(S)):
    if S[i] == "1":
        S[i] = ""
        rcnt += 1
        if rcnt == cnt1 // 2:
            break

rcnt = 0
for i in range(len(S)-1, -1, -1):
    if S[i] == "0":
        S[i] = ""
        rcnt += 1
        if rcnt == cnt0 // 2:
            break

print("".join(S))