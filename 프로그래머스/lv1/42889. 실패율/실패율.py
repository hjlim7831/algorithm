def solution(N, stages):
    cnt = [0 for _ in range(N + 2)]
    for n in stages:
        cnt[n] += 1
    
    stage_info = []
    user_cnt = len(stages)
    for i in range(1, N + 1):
        if user_cnt:
            stage_info.append((i, cnt[i], user_cnt))
        else:
            stage_info.append((i, cnt[i], 1))
        user_cnt -= cnt[i]
    
    stage_info.sort(key=lambda x: - x[1] / x[2])
    print(stage_info)
    answer = []
    
    for s in stage_info:
        answer.append(s[0])
    
    return answer