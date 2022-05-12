import sys
input = sys.stdin.readline

def back(st,num):
    if num == m:
        print(" ".join(map(str,ans)))
        return
    for i in range(st,n+1):
        ans.append(i)
        back(i,num+1)
        ans.pop()

ans = []
n, m = map(int,input().split())

back(1,0)
