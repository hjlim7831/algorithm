import sys
input = sys.stdin.readline

S = input().rstrip()
location = [-1 for _ in range(26)]

for idx in range(len(S)):
    num = ord(S[idx]) - ord("a")
    # print(num)
    if location[num] == -1:
        location[num] = idx

print(*location)