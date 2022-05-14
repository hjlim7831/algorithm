"""
아이디어
곱셈, 나눗셈을 먼저 하면 문제가 덜 생길 것 같다.
근데 계산된 값을 어떤식으로 처리해야 되지..?
값의 순서가 중요하긴 하니까, 리스트를 이용하긴 해야될 듯
리스트 사이에 끼워 넣어야되나?
-> 인덱스 처리가 중요할 듯

"""



import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
cal = list(map(int,input().split())) # +, -, *, /

# print(N, A)
# print(cal)

ans = []

def cal_p(num):
    if num == cal[0]:
        ans.append(A[0])
        return
    for i in range(len(A)-1):
        Ai, Ai1 = A[i], A[i+1]
        A[i] = Ai + Ai1
        A.pop(i+1)
        cal_p(num+1)
        A[i] = Ai
        A.insert(i+1,Ai1)

def cal_mi(num):
    if num == cal[1]:
        cal_p(0)
        return
    for i in range(len(A)-1):
        Ai, Ai1 = A[i], A[i+1]
        A[i] = Ai - Ai1
        A.pop(i+1)
        cal_mi(num+1)
        A[i] = Ai
        A.insert(i+1, Ai1)

def cal_m(num):
    if num == cal[2]:
        cal_mi(0)
        return
    for i in range(len(A)-1):
        Ai, Ai1 = A[i], A[i+1]
        A[i] = Ai*Ai1
        A.pop(i+1)
        cal_m(num+1)
        A[i] = Ai
        A.insert(i+1, Ai1)


def cal_d(num):
    if num == cal[3]:
        cal_m(0)
        return
    for i in range(len(A)-1):
        Ai, Ai1 = A[i], A[i+1]
        A[i] = Ai/Ai1
        A.pop(i+1)
        cal_d(num+1)
        A[i] = Ai
        A.insert(i+1, Ai1)


cal_m(0)
print(max(ans))
print(min(ans))