import sys, heapq
input = sys.stdin.readline

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def cal_R():
    global A
    tmp_A = []
    lr, lc = len(A), len(A[0])
    new_lc = 0
    for r in range(lr):
        cnt_arr = [0]*101
        for c in range(lc):
            val = A[r][c]
            if val == 0:
                continue
            cnt_arr[val] += 1
        new_row = []
        for num, cnt in enumerate(cnt_arr):
            if num == 0:
                continue
            if cnt == 0:
                continue
            new_row.append([num, cnt])
        if new_row:
            new_row.sort(key=lambda x:(x[1], x[0]))
        tmp_A.append(new_row)
        new_lc = max(new_lc, len(new_row))
    
    new_lc = min(new_lc, 50)

    new_A = [[0]*new_lc*2 for _ in range(lr)]

    # print("result of cal_R")
    for r in range(lr):
        for idx, [num, cnt] in enumerate(tmp_A[r][:new_lc]):
            new_A[r][idx*2] = num
            new_A[r][idx*2+1] = cnt
        # print(new_A[r])
    A = new_A
    return

def cal_C():
    global A
    tmp_At = []
    lr, lc = len(A), len(A[0])
    new_lr = 0
    for c in range(lc):
        cnt_arr = [0]*101
        for r in range(lr):
            val = A[r][c]
            if val == 0:
                continue
            cnt_arr[val] += 1
        new_col = []
        for num, cnt in enumerate(cnt_arr):
            if num == 0:
                continue
            if cnt == 0:
                continue
            new_col.append([num, cnt])
        if new_col:
            new_col.sort(key=lambda x:(x[1], x[0]))
        tmp_At.append(new_col)
        new_lr = max(new_lr, len(new_col))
    
    new_lr = min(new_lr, 100)
    new_A = [[0]*lc for _ in range(new_lr*2)]

    for c in range(lc):
        for idx, [num, cnt] in enumerate(tmp_At[c][:new_lr]):
            new_A[idx*2][c] = num
            new_A[idx*2+1][c] = cnt
    # print("result of cal_C")
    # for r in range(new_lr):
    #     print(new_A[r])
    A = new_A    
    return

duration = 0
while duration <= 100:
    # print("duration: ",duration)
    lr, lc = len(A), len(A[0])
    if r <= lr and c <= lc and A[r-1][c-1] == k:
        break

    if lr >= lc:
        cal_R()
    else:
        cal_C()

    duration += 1

if duration == 101:
    print(-1)
else:
    print(duration)