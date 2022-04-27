import sys
N = int(sys.stdin.readline())
array = [0] * 10001

for i in range(N):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)

# 역시나 input 자료들을 전부 저장하지 않는 것이 포인트였다..
# 이건 counting 정렬에 대해 제대로 이해해야 풀 수 있는 문제였던 것 같다.. 메모메모