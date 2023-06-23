import sys
input = sys.stdin.readline
N, L = map(int, input().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))
ans = 0
for r in range(N):
    acc_list = []
    pass_flag = False
    h = board[r][0]
    cnt = 1
    for c in range(1, N):
        # 높이가 같다면 
        if h == board[r][c]:
            cnt += 1
        # 높이가 1 차이 난다면
        elif abs(h - board[r][c]) == 1:
            acc_list.append((h, cnt))
            h = board[r][c]
            cnt = 1
        # 높이가 1 이상 차이난다면
        else:
            pass_flag = True
            break
    if pass_flag:
        continue
    acc_list.append((h, cnt))
    # print(acc_list)
    # 전부 다 높이가 같다면
    if len(acc_list) == 1:
        ans += 1
        continue
    ref_h, ref_cnt = acc_list[0]
    for idx, val in enumerate(acc_list[1:]):
        h, cnt = val
        if pass_flag:
            break
        if ref_h < h:
            if ref_cnt < L:
                pass_flag = True
            else:
                ref_cnt -= L
                acc_list[idx] = (ref_h, ref_cnt)
        else:
            if cnt < L:
                pass_flag = True
            else:
                cnt -= L
                acc_list[idx+1] = (h, cnt)
        ref_h, ref_cnt = h, cnt
    if pass_flag:
        continue
    # print(acc_list)
    ans += 1

# print(ans)
for c in range(N):
    acc_list = []
    pass_flag = False
    h = board[0][c]
    cnt = 1
    for r in range(1, N):
        # 높이가 같다면 
        if h == board[r][c]:
            cnt += 1
        # 높이가 1 차이 난다면
        elif abs(h - board[r][c]) == 1:
            acc_list.append((h, cnt))
            h = board[r][c]
            cnt = 1
        # 높이가 1 이상 차이난다면
        else:
            pass_flag = True
            break
    if pass_flag:
        continue
    acc_list.append((h, cnt))
    # print(acc_list)
    # 전부 다 높이가 같다면
    if len(acc_list) == 1:
        ans += 1
        continue
    ref_h, ref_cnt = acc_list[0]
    for idx, val in enumerate(acc_list[1:]):
        h, cnt = val
        if pass_flag:
            break
        if ref_h < h:
            if ref_cnt < L:
                pass_flag = True
            else:
                ref_cnt -= L
                acc_list[idx] = (ref_h, ref_cnt)
        else:
            if cnt < L:
                pass_flag = True
            else:
                cnt -= L
                acc_list[idx+1] = (h, cnt)
        ref_h, ref_cnt = h, cnt
    if pass_flag:
        continue
    # print(acc_list)
    ans += 1

print(ans)

