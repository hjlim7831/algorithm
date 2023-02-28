import sys
input = sys.stdin.readline

dft = -1_000_000_000

w_res = [[[dft for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a:int, b:int, c:int):
    global w_res, dft
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        if w_res[20][20][20] == dft:
            w_res[20][20][20] = w(20, 20, 20)
        return w_res[20][20][20]
    
    elif a < b and b < c:
        if w_res[a][b][c] == dft:
            w_res[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return w_res[a][b][c]
    
    else:
        if w_res[a][b][c] == dft:
            w_res[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return w_res[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")