import sys
input = sys.stdin.readline

N = int(input())
words = []

for _ in range(N):
    words.append(input().rstrip())

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for w in words:
    print(w)