import sys
input = sys.stdin.readline

N = int(input())
my_cards = list(map(int, input().split()))
card_dict = {}
for card in my_cards:
    if card in card_dict.keys():
        card_dict[card] = card_dict[card] + 1
    else:
        card_dict[card] = 1
# print(card_dict)

M = int(input())
chk_list = list(map(int, input().split()))

for chk in chk_list:
    if chk not in card_dict.keys():
        print(0, end=" ")
    else:
        print(card_dict[chk], end=" ")