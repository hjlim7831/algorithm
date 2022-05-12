"""
참조: https://www.youtube.com/watch?v=atTzqxbt4DM
아이디어
- 1부터 N중에 하나를 선택한 뒤
- 그 다음 1부터 N까지를 선택할 때, 이미 선택한 값이 아닌 경우를 선택
    -> 방문여부 체크하기
- M개를 선택할 경우, 프린트하기

"""

n, m = map(int,input().split())
rs = []
chk = [False]*(n+1)

def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(1,n+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)

            chk[i] = False
            rs.pop()

recur(0)