import sys
input = sys.stdin.readline

gear = []
for _ in range(4):
    gear.append(list(map(int, input().rstrip())))

K = int(input())
up_idx = [0]*4

# 같이 움직이는지 여부를 확인하는 함수
def rotate(l_num:int):
    l_idx = (up_idx[l_num] + 2) % 8
    r_idx = (up_idx[l_num + 1] - 2) % 8
    if gear[l_num][l_idx] + gear[l_num + 1][r_idx] == 1:
        return True
    else:
        return False

for _ in range(K):
    # 이번 회전에서 움직일 기어의 방향 저장
    step_rot = [0] * 4
    num, rot = map(int, input().rstrip().split())
    # 직접 움직이는 톱니 움직임 저장
    step_rot[num-1] = rot

    # 왼쪽 방향의 톱니 움직임 확인 및 저장
    l_num = num - 2
    l_rot = rot * -1
    while l_num >= 0 and rotate(l_num):
        step_rot[l_num] = l_rot
        l_num -= 1
        l_rot *= -1

    # 오른쪽 방향의 톱니 움직임 확인 및 저장
    l_num = num - 1
    l_rot = rot * -1
    while l_num + 1 <= 3 and rotate(l_num):
        step_rot[l_num + 1] = l_rot
        l_num += 1
        l_rot *= -1
    # print(step_rot)

    # 저장한 움직임대로 톱니 움직이기
    for idx, s in enumerate(step_rot):
        # 회전 시 방향은 - 붙여야 함
        up_idx[idx] = (up_idx[idx] - s) % 8
    # print(up_idx)

ans = 0
for i, val in enumerate(up_idx):
    ans += gear[i][val] * 2**i
print(ans)
