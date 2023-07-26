def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    
    left, right = 1, distance
    while left <= right:
        mid = (left + right) // 2
        del_cnt = 0
        front_stone = 0
        min_distance = float('inf')
        
        for rock in rocks:
            dist = rock - front_stone
            if dist < mid:
                del_cnt += 1
            else:
                front_stone = rock
                min_distance = min(min_distance, dist)                
        if del_cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = min_distance

    return answer