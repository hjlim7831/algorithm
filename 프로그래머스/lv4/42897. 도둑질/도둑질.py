def solution(money):
    lm = len(money)
    # [0] : 해당 집을 턴 경우에 가질 수 있는 최대값
    # [1] : 해당 집을 털지 않은 경우에 가질 수 있는 최대 값
    dp = [[0] * 2 for _ in range(lm)]
    dp[0][0] = money[0]
    dp[1][0] = money[1]
    dp[1][1] = money[0]
    
    dpx = [[0] * 2 for _ in range(lm)]
    dpx[1][0] = money[1]
    
    for i in range(2, lm):
        # [0]
        dp[i][0] = max(dp[i-1][1], dp[i-2][0], dp[i-2][1]) + money[i]
        dpx[i][0] = max(dpx[i-1][1], dpx[i-2][0], dpx[i-2][1]) + money[i]
        
        
        # [1]
        dp[i][1] = max(dp[i-1][0], dp[i-1][1], dp[i-2][0], dp[i-2][1])
        dpx[i][1] = max(dpx[i-1][0], dpx[i-1][1], dpx[i-2][0], dpx[i-2][1])
    
    # print(dp)
    # print(dpx)
    return max(dp[-1][1], dpx[-1][0])