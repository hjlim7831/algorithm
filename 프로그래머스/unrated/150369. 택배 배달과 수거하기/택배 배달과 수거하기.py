def solution(cap, n, deliveries, pickups):
    # cap : 트럭에 재활용 택배 상자를 최대 실을 수 있는 개수
    # 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리
    # 각 집에서 배달, 수거 시 원하는 개수만큼 택배를 배달, 수거 가능
    # deliveries : 배달할 재활용 택배 상자의 수
    # pickups : 수거할 빈 재활용 택배 상자의 수
    
    deliveries = [0] + deliveries
    pickups = [0] + pickups
    
    # 최대한 먼 곳부터 배달을 채워넣고, 돌아올 때 먼 곳에 있는 상자부터 수거해오기
    d_idx, p_idx = n, n
    
    dist = 0
    # 둘 다 0이 되면 끝내기
    while d_idx > 0 or p_idx > 0:
        # 0이 아닌 위치로 갱신하기
        while d_idx != 0 and deliveries[d_idx] == 0:
            d_idx -= 1
        while p_idx != 0 and pickups[p_idx] == 0:
            p_idx -= 1
        
        dist += max(d_idx, p_idx) * 2
        # print(d_idx, p_idx)
        # print(dist)
        
        # cap 개수만큼 제거하기
        p_rest, d_rest = cap, cap
        while d_rest != 0:
            if d_idx == 0:
                break
            if deliveries[d_idx] > d_rest:
                deliveries[d_idx] -= d_rest
                d_rest = 0
            else:
                d_rest -= deliveries[d_idx]
                deliveries[d_idx] = 0
                d_idx -= 1

        while p_rest != 0:
            if p_idx == 0:
                break
            if pickups[p_idx] > p_rest:
                pickups[p_idx] -= p_rest
                p_rest = 0
            else:
                p_rest -= pickups[p_idx]
                pickups[p_idx] = 0
                p_idx -= 1
        
    
    return dist