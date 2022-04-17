N = int(input())
score = list(map(int,input().split()))
Ms = max(score)
new_score = [0 for i in range(N)]
for i in range(N):
    new_score[i] = score[i]/Ms*100
print(sum(new_score)/N)