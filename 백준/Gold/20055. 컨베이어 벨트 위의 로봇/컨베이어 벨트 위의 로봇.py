import sys
input = sys.stdin.readline

N, K = map(int, input().split())

belt = list(map(int, input().split()))
robots = [0] * (2 * N)
on_pos = 0
off_pos = N-1

duration = 1
cnt_0 = 0

while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 회전
    # -> 로봇을 올리고 내리는 위치를 한 칸씩 뒤로 밀기
    on_pos = (on_pos - 1) % (2 * N)
    off_pos = (off_pos - 1) % (2 * N)
    # 만약 내리는 위치에 로봇이 도달하면 내리기
    robots[off_pos] = 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동시키기
    for i in range(N-2, -1, -1):
        pos = (on_pos + i) % (2 * N)
        next_pos = (pos + 1) % (2 * N)
        # print(pos, next_pos, end="  ")
        if robots[pos]:
            # print("pos: ",pos)
            if not robots[next_pos] and belt[next_pos]:
                robots[pos] = 0
                belt[next_pos] -= 1
                robots[next_pos] = 1
                if belt[next_pos] == 0:
                    cnt_0 += 1
                # 이동할 위치가 내리는 위치가 아니라면
                # 로봇 이동시키기
    robots[off_pos] = 0
    # 로봇 올리기
    if belt[on_pos] and not robots[on_pos]:
        robots[on_pos] = 1
        belt[on_pos] -= 1
        if belt[on_pos] == 0:
            cnt_0 += 1

    # print("duration: ", duration, "on:",on_pos, "off:",off_pos)
    # print(belt)
    # print(robots)
    
    if cnt_0 >= K:
        break
    
    duration += 1

print(duration)