import heapq

def solution(jobs):
    jobs.sort(key=lambda x:(x[0], x[1]))
    heap = [] # 현 시점에 들어온 요청들
    now, jidx = -1, 0
    answer = 0
    while True:
        while jidx < len(jobs) and jobs[jidx][0] <= now:
            heapq.heappush(heap, (jobs[jidx][1], jobs[jidx][0]))
            jidx += 1
        # print(now, heap)
        if not heap: # 들어온 요청이 없다면,
            heapq.heappush(heap, (jobs[jidx][1], jobs[jidx][0]))
            now = jobs[jidx][0]
            jidx += 1
        job_dur, job_st = heapq.heappop(heap)
        now += job_dur
        answer += now - job_st
        if jidx == len(jobs) and not heap:
            break
    answer //= len(jobs)
        
    return answer