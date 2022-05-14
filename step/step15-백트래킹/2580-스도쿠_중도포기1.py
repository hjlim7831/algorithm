from collections import deque

# 입력 받기
sudoku = []
for i in range(9):
    sudoku.append(list(map(int,input().split())))


index0 = deque() # sudoku 중 값이 0인 위치의 인덱스
solved0 = deque() # 값이 0이었던 인덱스 중, 내가 값을 집어넣은 위치 저장하기
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            index0.append([i,j,1])

# [i,j,n] 마지막 숫자 n은 다음번에 숫자를 n부터 넣으면서 시도하라는 뜻

# index가 (ii, jj)일 때, 그 열, 행, 사각형에 해당 숫자가 있는지 체크
def chk(ii,jj,num):
    srow = set(sudoku[ii])
    scol = set()
    for i in range(9):
        scol.add(sudoku[i][jj])
    i3, j3 = ii//3, jj//3
    square = set()
    for i in range(i3,i3+3):
        for j in range(j3,j3+3):
            square.add(sudoku[i][j])
    if num in srow:
        return False
    if num in scol:
        return False
    if num in square:
        return False
    return True

sti, stj, stn = index0.popleft()
i, j = sti, stj

while index0:
    for n in range(stn,10):
        if chk(i,j,n):
            sudoku[i][j] = n
            solved0.append([i,j,n])
            sti, stj, stn = index0.popleft()
            i,j = sti, stj
            continue
    index0.append([i,j,1])
    i, j, stn = index0.popleft()
    if sti == i and stj == j:
        sti, stj, stn = solved0.pop()
        i, j = sti, stj

print(" ")
for i in range(9):
    print(" ".join(map(str,sudoku[i])))


"""
queue로 0인 위치를 순회하면서 일단 되는 값을 넣은 뒤,
값을 집어넣은 index를 stack에 쌓아두고
후에 더 이상 진행이 안되거나 모순만 계속 나타나면
stack에서 다시 꺼내면서 모순이 발생하지 않는 위치를 찾으려고 했는데..
좀 어렵다..

"""