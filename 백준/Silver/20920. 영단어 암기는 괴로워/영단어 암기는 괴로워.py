import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

raw_words = [input().rstrip() for _ in range(N)]

words_dict = defaultdict(int)

for w in raw_words:
    words_dict[w] += 1

words = []

for w in words_dict.keys():
    if len(w) >= M:
        words.append((words_dict[w], w))

words.sort(key=lambda x:(-x[0], -len(x[1]), x[1]))
for n, w in words:
    print(w)