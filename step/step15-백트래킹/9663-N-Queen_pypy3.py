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

# 음... PyPy3로 제출하니까 맞았다..??
# 그리고 왜인지 시간도 더 짧게 걸렸다..???
# 그리고 왜 메모리도 더 적게 쓰였지..? 이상한데..???
# 아 PyPy3는 복잡할수록 더 효과가 좋다던데 이래서 그런건가..? (아닐 가능성 99%)
# 아니 근데 그냥 알고리즘 형태만 봐도 이게 훨씬 복잡한데..?? 뭐지?