import sys
input = sys.stdin.readline

N = int(input())

if N:
    scores = [int(input()) for _ in range(N)]
    scores.sort()
    d_val = N * 3 / 20
    d = int(d_val)
    if d_val - d >= 0.5:
        d += 1
        
    score_val = sum(scores[d:N-d]) / (N - 2 * d)
    score = int(score_val)
    if score_val - score >= 0.5:
        score += 1

    print(score)

else:
    print(0)