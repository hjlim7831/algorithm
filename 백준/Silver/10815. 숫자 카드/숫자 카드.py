import sys
input = sys.stdin.readline

N = int(input())
my_cards = set(map(int, input().split()))

M = int(input())
check_list = list(map(int, input().split()))

for chk in check_list:
    if chk in my_cards:
        print(1, end=" ")
    else:
        print(0, end=" ")