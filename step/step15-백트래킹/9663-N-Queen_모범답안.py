N = int(input())
ans = 0
chk = [0]*N


def queen_check(num):
    for i in range(num):
        if chk[num] == chk[i] or \
            abs(chk[num] - chk[i]) == abs(num-i):
            return False
    return True


def back(num):
    global ans
    if num == N:
        ans += 1
        return
    for i in range(N):
        chk[num] = i
        if queen_check(num):
            back(num+1)
back(0)
print(ans)

# 리스트의 index와 value로 2차원 체스판을..
# 하긴 내가 한 방식은 3차원 contour나 다름이 없었구나..
# 그 정도의 정보까지는 필요 없었는데.
# 백트래킹을 할 때, 값을 구한 이후 그 다음 값을 구할 때,
# 이전에 구한 답이 영향을 주면 안되는데
# 여기서는 그냥 True/False로 체크만 하고 맞는 경우에만 다음 단계로 넘어가며
# 틀린 경우 그 값을 그냥 덮어 씌워버리니까 훨씬 더 간결해진듯.
# 내 경우에는 트랙을 남기고, 그걸 지우는 과정에 모두 for 문이 들어갔으니..
# .. 근데 왜 이것도 시간초과가 뜨지..?
# 찾아보니 python3로는 통과가 되지 않고, pypy3로 제출하면 통과된다고 한다..
# 이렇게 해야 하는건가..?
#다시풀기
