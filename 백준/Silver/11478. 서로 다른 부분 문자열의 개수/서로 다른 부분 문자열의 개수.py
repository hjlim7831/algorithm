import sys
input = sys.stdin.readline

S = input().rstrip()

substr_set = set()

len_S = len(S)

for i in range(len_S):
    for j in range(i+1, len_S+1):
        substr_set.add(S[i:j])

print(len(substr_set))