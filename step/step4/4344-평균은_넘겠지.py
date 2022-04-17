C = int(input())
for i in range(C):
    tot_list = list(map(int,input().split()))
    N = tot_list[0]
    score_list = tot_list[1:]
    m = sum(score_list)/N
    over_list = [st for st in score_list if st>m]
    ratio = len(over_list)/N*100
    print(f"{ratio:.3f}%")