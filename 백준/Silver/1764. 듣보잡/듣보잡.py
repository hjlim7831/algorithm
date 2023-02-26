import sys
input = sys.stdin.readline

N, M = map(int, input().split())
set1 = set()
set2 = set()

for _ in range(N):
    set1.add(input().rstrip())

for _ in range(M):
    set2.add(input().rstrip())

inter = set1.intersection(set2)
inter_list = list(inter)
inter_list.sort()

print(len(inter))
for person in inter_list:
    print(person)