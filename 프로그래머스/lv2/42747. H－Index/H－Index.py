def solution(citations):
    citations.sort()

    l_cit = len(citations)
    
    answer = 0
    # 0회 ~ 첫 번째 논문 기준
    if 0 < l_cit <= citations[0]:
        answer = l_cit
    else:
        for idx in range(1, l_cit):
            if l_cit-idx <= citations[idx]:
                answer = l_cit - idx
                break
    
    return answer