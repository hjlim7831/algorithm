import sys
input = sys.stdin.readline

N, opt = input().rstrip().split()

cnt = -1
if opt == "Y":
    cnt = 1
elif opt == "F":
    cnt = 2
elif opt == "O":
    cnt = 3

p_set = set()
for _ in range(int(N)):
    p_set.add(input().rstrip())

print(len(p_set) // cnt)
