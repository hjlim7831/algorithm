def solution(n, m, section):
    # n : 벽의 구역 수
    # m : 롤러의 길이 (한 번 칠할 때의 길이)
    # section : 칠해야 하는 구역
    # 칠한 곳을 다시 칠해도 되고, 안 칠해도 되는 곳도 다시 칠해도 됨
    # 그냥 처음부터 쭉 밀면서 풀면 문제가 생길까?
    wall = [True for _ in range(n)]
    for s in section:
        wall[s - 1] = False
    cnt = 0
    for s in section:
        if not wall[s - 1]:
            cnt += 1
            for i in range(s - 1, s + m - 1):
                if i >= n:
                    break
                wall[i] = True
    
    return cnt