import sys
N, M = map(int,sys.stdin.readline().split())

set_N = set()
set_M = set()
for i in range(N):
    set_N.add(sys.stdin.readline().rstrip())

for i in range(M):
    set_M.add(sys.stdin.readline().rstrip())

list_NM = list(set_N & set_M)
list_NM.sort()
print(len(list_NM))
for i in list_NM:
    print(i)
