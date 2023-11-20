import sys
input = sys.stdin.readline

N, M = map(int, input().split())

keywords = set([input().rstrip() for _ in range(N)])

for _ in range(M):
    words = input().rstrip().split(",")
    for w in words:
        if w in keywords:
            keywords.remove(w)
    print(len(keywords))