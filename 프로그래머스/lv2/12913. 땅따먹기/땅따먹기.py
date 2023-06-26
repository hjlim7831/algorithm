def solution(land):
    l = len(land)
    dp = [[0] * 4 for _ in range(l)]
    
    # 초기값 저장
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1, l):
        for n in range(4):
            max_score = 0
            for op in range(4):
                if n == op:
                    continue
                max_score = max(max_score, dp[i-1][op])
            dp[i][n] = max_score + land[i][n]
            
    return max(dp[-1])