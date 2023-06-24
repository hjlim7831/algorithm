def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr1[0])
    k = len(arr2[0])
    answer = [[0]*k for _ in range(n)]
    
    for r in range(n):
        for c in range(k):
            for l in range(m):
                answer[r][c] += arr1[r][l]*arr2[l][c]
    return answer