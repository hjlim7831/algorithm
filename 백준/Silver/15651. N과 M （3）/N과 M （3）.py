import sys
input = sys.stdin.readline

def back(num):
    if num == m:
        print(" ".join(map(str,ans)))
        return
    for i in range(1,n+1):
        ans.append(i)
        back(num+1)
        ans.pop()

ans = []
n, m = map(int,input().split())
back(0)