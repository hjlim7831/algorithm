import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    words = input().rstrip().split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    print(*words)
