import sys
input = sys.stdin.readline

S = input().rstrip()

alpha_acc = [[0]*26 for _ in range(len(S))]

alpha_acc[0][ord(S[0]) - ord('a')] = 1

for i in range(1, len(S)):
    for j in range(26):
        if j == ord(S[i]) - ord('a'):
            alpha_acc[i][j] = alpha_acc[i-1][j] + 1
        else:
            alpha_acc[i][j] = alpha_acc[i-1][j]

alpha_acc = [[0]*26] + alpha_acc

q = int(input())

for _ in range(q):
    alpha, l, r = input().rstrip().split()
    alp_ind = ord(alpha) - ord('a')
    print(alpha_acc[int(r)+1][alp_ind] - alpha_acc[int(l)][alp_ind])