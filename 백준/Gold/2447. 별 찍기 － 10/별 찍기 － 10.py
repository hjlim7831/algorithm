import sys
input = sys.stdin.readline

N = int(input())

star = [[" " for _ in range(N)] for _ in range(N)]

def rec(x:int, y:int, siz:int):
    # print(x, y, siz)
    if siz == 3:
        for i in range(x, x+3):
            for j in range(y, y+3):
                if i == x+1 and j == y+1:
                    continue
                star[i][j] = "*"
        return
    new_siz = siz//3
    rec(x, y, new_siz)
    rec(x+new_siz, y, new_siz)
    rec(x+new_siz*2, y, new_siz)
    rec(x, y+new_siz, new_siz)
    rec(x+new_siz*2, y+new_siz, new_siz)
    rec(x, y+new_siz*2, new_siz)
    rec(x+new_siz, y+new_siz*2, new_siz)
    rec(x+new_siz*2, y+new_siz*2, new_siz)

rec(0, 0, N)
for i in range(N):
    print(*star[i], sep="")