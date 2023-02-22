import sys
input = sys.stdin.readline

board = [["" for _ in range(15)] for _ in range(5)]

for r in range(5):
    word = input().rstrip()
    for c in range(len(word)):
        board[r][c] = word[c]

ans = ""
for c in range(15):
    for r in range(5):
        if board[r][c] == "":
            continue
        ans += board[r][c]

print(ans)