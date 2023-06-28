cnt = 0

def solution(n):
    chess = [0 for _ in range(n)]
    cnt = dfs(0, chess, n)
    return cnt

def dfs(depth:int, chess:list, n:int):
    count = 0
    if depth == n:
        return 1
    for pos in range(n):
        flag = True
        chess[depth] = pos
        for j in range(depth):
            if chess[j] == chess[depth]:
                flag = False
                break
            if depth - j == abs(chess[depth] - chess[j]):
                flag = False
                break
        if flag:
            count += dfs(depth + 1, chess, n)
    return count