import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = list(map(int, input().split()))

for i in range(N-1):
    vals = list(map(int, input().split()))
    heap += vals
    heapq.heapify(heap)
    for _ in range(N):
        heapq.heappop(heap)

print(heapq.heappop(heap))