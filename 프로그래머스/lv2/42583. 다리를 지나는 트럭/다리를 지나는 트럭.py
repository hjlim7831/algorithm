from collections import deque

def solution(bridge_length, weight, truck_weights):
    duration, w_sum = 0, 0
    bridge = deque()
    wait_que = deque()
    for t in truck_weights:
        wait_que.append(t)
    
    
    while wait_que or bridge:
        if bridge and bridge[0][1] == duration:
            truck, d = bridge.popleft()
            w_sum -= truck
        
        if wait_que:
            tmp_weight = wait_que[0] + w_sum
            if len(bridge) < bridge_length and tmp_weight <= weight:
                truck = wait_que.popleft()
                bridge.append((truck, duration + bridge_length))
                w_sum += truck
        duration += 1
    return duration