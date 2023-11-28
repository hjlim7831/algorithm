import sys
input = sys.stdin.readline

number = input().rstrip()

trans_dict = {}

for i in range(10):
    trans_dict[str(i)] = i

for i in range(6):
    trans_dict[chr(ord("A") + i)] = i + 10

answer = 0
for n in number:
    answer *= 16
    answer += trans_dict[n]

print(answer)
    

