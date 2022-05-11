import sys

An, Bn = map(int,sys.stdin.readline().split())
A = set(map(int,sys.stdin.readline().split()))
B = set(map(int,sys.stdin.readline().split()))

AB = (A - B) | (B - A)
print(len(AB))