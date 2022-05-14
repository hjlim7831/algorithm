"""
순서대로 계산.. 거기에 나눗셈은 정수 나눗셈만 침
"""
# 문제 대충 읽고 넘겨짚지 말자
# 음수 나눗셈에서 //를 사용할 경우,
# '버림'이 내가 원하는 방향대로 이루어지지 않음
# insert 방법 잘 익혀두기

# 타 답안을 보다보니까, 굳이 A라는 리스트의 형태를
# 바꿔가면서 할 필요가 없어보인다..? 그냥 값 뽑아서 가져다 쓰면...



import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
cal = list(map(int,input().split())) # +, -, *, /

# print(N, A)
# print(cal)

ans = []
own_cal = [0,0,0,0]

def calc(num):
    if num == N-1:
        ans.append(A[0])
        return
    A0, A1 = A[0], A[1]

    if own_cal[0] < cal[0]:
        own_cal[0] += 1
        A[0] = A0+A1
        A.pop(1)
        calc(num+1)
        A[0] = A0
        A.insert(1,A1)
        own_cal[0] -= 1

    if own_cal[1] < cal[1]:
        own_cal[1] += 1
        A[0] = A0-A1
        A.pop(1)
        calc(num+1)
        A[0] = A0
        A.insert(1,A1)
        own_cal[1] -= 1

    if own_cal[2] < cal[2]:
        own_cal[2] += 1
        A[0] = A0*A1
        A.pop(1)
        calc(num+1)
        A[0] = A0
        A.insert(1,A1)
        own_cal[2] -= 1

    if own_cal[3] < cal[3]:
        own_cal[3] += 1
        if A0/A1 < 0:
            res = abs(A0)//A1
            A[0] = -res
        else:
            A[0] = A0//A1
        A.pop(1)
        calc(num+1)
        A[0] = A0
        A.insert(1,A1)
        own_cal[3] -= 1

calc(0)

# print(ans)
# print(len(ans))
print(max(ans))
print(min(ans))