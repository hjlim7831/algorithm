import sys
input = sys.stdin.readline

# N : 도감에 수록되어 있는 포켓몬의 개수
# M : 내가 맞춰야 하는 문제의 개수
N, M = map(int, input().split())

num_to_name = {}
name_to_num = {}

for num in range(1, N+1):
    name = input().rstrip()
    num_to_name[num] = name
    name_to_num[name] = num

for i in range(M):
    question = input().rstrip()
    if ord('0') <= ord(question[0]) <= ord('9'):
        print(num_to_name[int(question)])
    else:
        print(name_to_num[question])