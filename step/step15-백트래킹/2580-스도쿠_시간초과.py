"""
아이디어
0인 위치마다 가로, 세로, 사각형을 확인하면서 들어갈 수 있는 값을
찾아서 리스트로 적어 놓기
그 리스트의 경우의 수들을 체크하면서 올바른 스도쿠의 모습을 찾기

"""
# 타 답안과 아이디어는 꽤 비슷했는데, 속도 차이가 난다. 왜일까?
# 나는 1부터 10까지 모든 숫자를 집어넣는 것이 아니라, 미리 note를 적어두고
# 그 중에서 값을 골라 집어넣는 형식이었는데
# 그런 노트를 만드는 것 자체가 오래걸렸을 수도 있겠다.

# 타 답안에서는 그냥 1부터 10까지 전부 집어넣는 대신, row, col, rect에
# 그 값이 있는지 없는지를 '체크'만 했다.
# (나는 add에 합집합에 차집합..을 했으니까 그 차이가 나타난 듯 하다.)

import sys

# 입력 받기
sudoku = []
for i in range(9):
    sudoku.append(list(map(int,sys.stdin.readline().split())))

index0 = []
note0 = []

def note(ii,jj):
    srow = set(sudoku[ii])
    scol = set()
    for i in range(9):
        scol.add(sudoku[i][jj])
    square = set()
    i3, j3 = ii//3, jj//3
    for i in range(i3*3,i3*3+3):
        for j in range(j3*3,j3*3+3):
            square.add(sudoku[i][j])
    res = set([i for i in range(1,10)]) - (srow|scol|square)
    return res


for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            index0.append((i,j))
            note_temp = list(note(i,j))
            note_temp.sort()
            note0.append(note_temp)

#print(index0)

num0 = len(index0)

def back(num):
    if num == num0:
        for i in range(9):
            print(' '.join(map(str,sudoku[i])))
        return
    ii, jj = index0[num]
    note_temp = note0[num]
    for n in note_temp:
        if n in note(ii,jj):
            sudoku[ii][jj] = n
            back(num+1)
            sudoku[ii][jj] = 0

back(0)
