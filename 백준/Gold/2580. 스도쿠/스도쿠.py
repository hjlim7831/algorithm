import sys
input = sys.stdin.readline

sudoku = []
r_list = []
c_list = []

for r in range(9):
    sudoku.append(list(map(int, input().split())))
    for c in range(9):
        if sudoku[r][c] == 0:
            r_list.append(r)
            c_list.append(c)

len_chk = len(r_list)
flag = False

def make_sudoku(idx:int):
    # print(idx)
    global flag, sudoku
    if idx == len_chk:
        flag = True
        return
    r_now = r_list[idx]
    c_now = c_list[idx]

    chk_set = set(sudoku[r_now])

    for r in range(9):
        chk_set.add(sudoku[r][c_now])
    
    r_sq = r_now // 3 * 3
    c_sq = c_now // 3 * 3
    for r in range(r_sq, r_sq+3):
        for c in range(c_sq, c_sq+3):
            chk_set.add(sudoku[r][c])

    # print(chk_set)

    for num in range(1, 10):
        if num not in chk_set:
            # print(num)
            sudoku[r_now][c_now] = num
            make_sudoku(idx+1)
            if flag:
                break
            sudoku[r_now][c_now] = 0

make_sudoku(0)

for i in range(9):
    print(*sudoku[i])

