import sys
input = sys.stdin.readline

len_A, len_B = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

A_B = A - B
B_A = B - A
# print(A_B, B_A)

ans = A_B.union(B_A)
print(len(ans))