# 수업 듣고 직접 풀어본 것
import sys

def back(num):
    if num == m:
        print(' '.join(map(str,ans)))
        return
    for i in range(1,n+1):
        if not chk[i]:
            chk[i] = True
            ans.append(i)
            back(num+1)
            chk[i] = False
            ans.pop()



input = sys.stdin.readline
n, m = map(int,input().split())

ans = []
chk = [False]*(n+1)

back(0)