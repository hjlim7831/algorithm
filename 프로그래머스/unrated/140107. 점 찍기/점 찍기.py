def solution(k, d):
    cnt = 0
    for l in range(0, d + 1, k):
        r = int((d**2 - l**2)**0.5)
        cnt += (r // k) + 1
            
    return cnt