import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [input().rstrip() for _ in range(R)]

answer = [0] * 9
remove_set = set()
remove_set.add(".")

rank = 1
for c in range(C-2, 0, -1):
    exist_flag = False
    for r in range(R):
        if graph[r][c] not in remove_set:
            boat = int(graph[r][c])
            exist_flag = True
            answer[boat-1] = rank
            remove_set.add(graph[r][c])
    if exist_flag:
        rank += 1

for i in range(9):
    print(answer[i])