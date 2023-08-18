def solution(n):
    if n <= 2:
        return n
    DIV = 1_000_000_007
    dp = [0]*n
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % DIV
    
    return dp[-1]