import sys
N = int(sys.stdin.readline())
array = []
for i in range(N):
    x, y = map(int,sys.stdin.readline().split())
    array.append([y,x])

sarray = sorted(array)

for y, x in sarray:
    print(x,y)

# 어레이 속 어레이를 이용할 경우, 바깥 어레이에서 sorted를 쓰면 그 내부 어레이의 첫 요소를 기준으로 정렬을 하나보다..!
# 그리고 그 첫 요소가 같으면, 그 다음 요소를 기준으로 정렬을 하는듯..?
# 나중에 이용하기 좋을 듯