import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)

for _ in range(m):
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)
    c = c1 + c2
    heapq.heappush(cards, c)
    heapq.heappush(cards, c)

print(sum(cards))

