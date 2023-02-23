import sys
input = sys.stdin.readline

rec = 0

def recursion(s:str, l:int, r:int):
    global rec
    rec += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s:str):
    return recursion(s, 0, len(s)-1)


T = int(input())

for _ in range(T):
    S = input().rstrip()
    rec = 0
    res = isPalindrome(S)
    print(res, rec)