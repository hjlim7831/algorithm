def solution(m, n, puddles):
    div = 1_000_000_007
    
    pud_visit = set()
    for c, r in puddles:
        pud_visit.add((r, c))
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for r in range(1, n+1):
        for c in range(1, m+1):
            if r == 1 and c == 1:
                continue
            pos = (r, c)
            if pos in pud_visit:
                dp[r][c] = 0
            else:
                dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % div
    # print(dp)
    return dp[-1][-1]