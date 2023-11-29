import sys
input = sys.stdin.readline

code = list(map(int, input().rstrip()))
DIV = 1_000_000

lc = len(code)

def chk_len1(idx:int):
    if code[idx] == 0:
        return False
    return True

def chk_len2(idx:int):
    num = code[idx-1] * 10 + code[idx]
    if 10 <= num <= 26:
        return True
    return False

dp = [0] * lc

for i in range(lc):
    if i == 0:
        if chk_len1(i):
            dp[i] = 1
    elif i == 1:
        if chk_len1(i):
            dp[i] += 1
        if chk_len2(i):
            dp[i] += 1
    else:
        if chk_len1(i):
            dp[i] = (dp[i] + dp[i-1]) % DIV
        if chk_len2(i):
            dp[i] = (dp[i] + dp[i-2]) % DIV
    if dp[i] == 0:
        break
# print(dp)
print(dp[-1])