import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    files_acc = [0]*(K+1)
    for i in range(K):
        files_acc[i+1] = files_acc[i] + files[i]
    dp = [[float("inf")]*K for _ in range(K)]
    for i in range(K):
        dp[i][i] = 0
    
    for l in range(2, K+1):
        for st in range(K-l+1):
            ed = st + l - 1
            tot_file = files_acc[ed+1] - files_acc[st]
            for mid in range(st, ed):
                cost = dp[st][mid] + dp[mid+1][ed] + tot_file
                dp[st][ed] = min(dp[st][ed], cost)
    # for i in range(K):
    #     print(dp[i])
    print(dp[0][-1])


