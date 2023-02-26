import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chess = []
for _ in range(N):
    chess.append(input().rstrip())

min_val = 64
for st_r in range(N - 7):
    for st_c in range(M - 7):
        p1 = 0; p2 = 0
        for r in range(st_r, st_r + 8):
            for c in range(st_c, st_c + 8):
                crit = (r + c) % 2
                if crit:
                    if chess[r][c] == 'W':
                        p1 += 1
                    else:
                        p2 += 1
                else:
                    if chess[r][c] == 'B':
                        p1 += 1
                    else:
                        p2 += 1
        min_val = min(min(p1, p2), min_val)

print(min_val)