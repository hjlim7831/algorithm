import sys

K, N = map(int,sys.stdin.readline().split())
lan = [0 for i in range(K)]

for i in range(K):
    lan[i] = int(sys.stdin.readline())

start, end = 1, max(lan)

while start<=end:
    mid = (start + end)//2
    lines = 0
    for i in lan:
        lines += i // mid
    
    if lines >= N:
        start = mid + 1
    else:
        end = mid -1
print(end)

# 잘 기억해 두자. 시간 초과가 날 것 같을 때에 활용하기 좋을 듯