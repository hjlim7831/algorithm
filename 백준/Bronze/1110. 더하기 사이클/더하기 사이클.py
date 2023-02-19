import sys
import copy
input = sys.stdin.readline


N = input().rstrip() # 숫자를 문자열로 입력받기

cycle = 0 # cycle 횟수
now = copy.copy(N) # 문자열 얕은 복사
while True:
    cycle += 1
    if len(now) == 1: # 한 자리 수일 때
        now = "0" + now # 십의 자리 수에 0 추가
    sum = int(now[0]) + int(now[1])
    next = str(now[1]) + str(sum % 10)
    # print(next)
    if int(next) == int(N): # next는 무조건 두 자리 수
        break;
    now = next
print(cycle)