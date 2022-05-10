N = int(input())
card_number = set(map(int,input().split()))
M = int(input())
det_number = list(map(int,input().split()))

for i in range(M):
    if det_number[i] in card_number:
        print(1,end=" ")
    else:
        print(0,end=" ")