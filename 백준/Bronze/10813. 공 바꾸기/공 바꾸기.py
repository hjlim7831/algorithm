import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basket = [i for i in range(N+1)]

def swap(i, j):
    basket[j], basket[i] = basket[i], basket[j]

for _ in range(M):
    i, j = map(int, input().split())
    swap(i, j)

print(*basket[1:])