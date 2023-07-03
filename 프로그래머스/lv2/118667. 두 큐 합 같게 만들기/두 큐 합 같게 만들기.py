from collections import deque

def solution(queue1, queue2):
    total_sum = sum(queue1) + sum(queue2)
    target_sum = total_sum // 2
    total_len = len(queue1) + len(queue2)
    
    # total_sum이 홀수일 경우
    if total_sum != target_sum * 2:
        return -1
    
    # 이미 두 큐에 담긴 원소의 합이 같다면
    if sum(queue1) == target_sum:
        return 0
    
    que1, que2 = deque(queue1), deque(queue2)
    tmp_sum1 = sum(queue1)
    cnt = 0
    while cnt < total_len * 2:
        if tmp_sum1 > target_sum:
            num = que1.popleft()
            que2.append(num)
            tmp_sum1 -= num
        elif tmp_sum1 < target_sum:
            num = que2.popleft()
            que1.append(num)
            tmp_sum1 += num
        else:
            break
        cnt += 1
    
    if cnt == total_len * 2:
        return -1
        
    return cnt