import sys
N = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))

xset = list(set(x))
xset.sort()

dic = {xset[i]:i for i in range(len(xset))}

for j in x:
    print(dic[j], end=" ")

# list.index는 O(N)의 시간복잡도를 갖는다.
# dict[i]는 O(1)의 시간복잡도를 갖는다.
# 카운팅 정렬을 할까 하다가 메모리 걱정이 되기도 하고 시간 단축이 딱히 안될 것 같아서 고민했는데, 타당한 걱정이었던 것 같다.
# 다시풀기