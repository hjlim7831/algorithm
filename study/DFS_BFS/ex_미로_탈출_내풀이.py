# 출처: https://www.youtube.com/watch?v=7C9RgOcvkvo
"""
문제
- 동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혔습니다.
미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야합니다.
- 동빈이의 위치는 (1,1)이며 미로의 출구는 (N, M)의 위치에 존재하며
한 번에 한 칸씩 이동할 수 있습니다. 이 때 괴물이 있는 부분은 0으로,
괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출할 수 있는
형태로 제시됩니다.
- 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.
"""

def dfs(i,j,move):
    if 0 <= i <= n-1 and 0 <= j <= m-1:
        if maze[i][j] == 1:
            maze[i][j] = move
            # print(i,j)
            dfs(i+1,j,move+1)
            dfs(i,j+1,move+1)
            dfs(i-1,j,move+1)
            dfs(i,j-1,move+1)

n, m = map(int,input().split())
maze = []
for i in range(n):
    maze.append(list(map(int,input())))

dfs(0,0,1)
print(maze[n-1][m-1])

# BFS는 아닌거 같은데..? DFS인가.. 재귀니까 DFS인가보다.
# 예시 답안은 맞았지만 틀린 듯. 출구를 최단 거리 방법이 아닌 다른 방법으로
# 먼저 도달할 수도 있을 것 같다.. 가령 출구가 (6,0) 이었다면 답이 틀렸을 듯