import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
avg_score = sum(score) / len(score)
ans = avg_score / max_score * 100

print(ans)