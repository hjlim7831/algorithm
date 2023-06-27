def solution(n, k):
    perm = [1]
    for i in range(2, n):
        perm.append(perm[-1] * i)
    print(perm)
    
    rank = []
    
    num = k - 1
    for i in range(len(perm)-1, -1, -1):
        rank.append((num // perm[i]) + 1)
        num = num % perm[i]
    print(rank)
    
    answer = []
    
    used = set()
    
    for s_num in rank:
        cnt = 0
        for num in range(1, n + 1):
            if num in used:
                continue
            cnt += 1
            if cnt == s_num:
                used.add(num)
                answer.append(num)
    last = set([i for i in range(1, n + 1)]) - used
    for num in last:
        answer.append(num)
    
    
    return answer