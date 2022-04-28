import sys
N = int(sys.stdin.readline())
nn = list(map(int, sys.stdin.readline().split()))

print(min(nn)*max(nn))