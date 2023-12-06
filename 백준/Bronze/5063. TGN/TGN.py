import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    r, e, c = map(int, input().split())
    adv_tot = e - c
    if r > adv_tot:
        print("do not advertise")
    elif r < adv_tot:
        print("advertise")
    else:
        print("does not matter")