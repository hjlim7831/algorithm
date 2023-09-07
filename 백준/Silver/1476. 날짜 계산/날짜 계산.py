import sys
input = sys.stdin.readline

divE, divS, divM = 15, 28, 19

E, S, M = map(int, input().split())

E %= divE
S %= divS
M %= divM

year = 1
nE, nS, nM = 1, 1, 1

while True:
    if nE == E and nS == S and nM == M:
        break
    nE = (nE + 1) % divE
    nS = (nS + 1) % divS
    nM = (nM + 1) % divM
    year += 1

print(year)