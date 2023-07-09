def solution(triangle):
    lt = len(triangle)
    
    dp = [[triangle[0][0]]]
    for i in range(1, lt):
        # print(i)
        dp_row = []
        dp_row.append(dp[i-1][0] + triangle[i][0])
        for j in range(1, i):
            dp_row.append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
        dp_row.append(dp[i-1][-1] + triangle[i][-1])
        dp.append(dp_row)
    return max(dp[-1])