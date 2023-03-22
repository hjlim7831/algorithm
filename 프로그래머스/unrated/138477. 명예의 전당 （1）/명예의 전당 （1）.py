from queue import PriorityQueue

def solution(k, score):
    pq = PriorityQueue(maxsize = k + 1)
    answer = []
    for s in score:
        pq.put(s)
        if pq.full():
            pq.get()
        answer.append(pq.queue[0])    
    
    return answer