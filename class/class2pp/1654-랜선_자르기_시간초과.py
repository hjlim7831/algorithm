import sys

K, N = map(int,sys.stdin.readline().split())
lan = [0 for i in range(K)]

maxl = 0
for i in range(K):
    lan[i] = int(sys.stdin.readline())
    maxl += lan[i]/N
maxl = int(maxl)


while True:
    n = 0
    for i in range(K):
        n += lan[i]//maxl
    if n >= N:
        print(maxl)
        break
    maxl -= 1