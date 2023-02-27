N = int(input())
ans = 0
chk = [[0]*N for _ in range(N)]


def queen_check(i,j,n):
    for it in range(N):
        chk[it][j] += n
    ii, jj = i+1, j+1
    while ii < N and jj < N:
        chk[ii][jj] += n
        ii += 1
        jj += 1
    ii, jj = i+1, j-1
    while ii < N and jj >= 0:
        chk[ii][jj] += n
        ii += 1
        jj -= 1


def back(num):
    global ans
    if num == N:
        ans += 1
#        print(ans)
#        print(location)
        return
    for i in range(N):
        if chk[num][i] == 0:
#            location.append([num,i])
            queen_check(num,i,1)
            back(num+1)
#            location.pop()
            queen_check(num,i,-1)

#location = []
back(0)
print(ans)