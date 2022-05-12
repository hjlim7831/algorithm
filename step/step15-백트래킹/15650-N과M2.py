import sys
input = sys.stdin.readline

def back(st,num):
    if num == m:
        print(" ".join(map(str,ans)))
        return # 마지막에 이거 빼먹지 않기!!!
    if st > n:
        return
    for i in range(st,n+1):
        ans.append(i)
        back(i+1,num+1)
        ans.pop()

n, m = map(int,input().split())

ans = []

back(1,0)