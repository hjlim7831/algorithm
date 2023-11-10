import sys
from collections import deque
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

que = deque([T])
answer = 0
while que:
    # print(que)
    word = que.popleft()
    if len(word) == len(S):
        if word == S:
            answer = 1
            break
        continue
    if word[-1] == "A":
        que.append(word[:-1])
    if word[0] == "B":
        tmp_word = word[-1:0:-1]
        que.append(tmp_word)

print(answer)