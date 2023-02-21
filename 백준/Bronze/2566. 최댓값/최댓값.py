import sys
input = sys.stdin.readline

num_max = -1
idxi, idxj = -1, -1
for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(9):
        if num_max < tmp[j]:
            num_max = tmp[j]
            idxi, idxj = i, j

print(num_max)
print(idxi+1, idxj+1)