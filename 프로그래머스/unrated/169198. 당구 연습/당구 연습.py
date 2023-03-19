def solution(m, n, startX, startY, balls):
    # m : 당구대의 가로 길이, n : 당구대의 세로 길이
    # startX, startY : 칠 공의 위치
    # balls : 맞춰야 하는 공의 위치
    # 무조건 원 쿠션은 해야 함 (거리는 최소가 되어야)
    answer = []
    for x, y in balls:
        # 꼭짓점에 맞을 때
        # 1. x : y = startX : startY
        min_len = 5_000_000
        if y * startX == x * startY and startX < x:
            min_len = min(min_len, x**2+y**2+startX**2+startY**2)
        # 2. (m - x) : y = (m - startX) : startY
        if (m - x) * startY == y * (m - startX) and startY < y:
            min_len = min(min_len, (m - x) ** 2 + y ** 2 + (m - startX) ** 2 + startY ** 2)
        # 3. x : (n - y) = startX : (n - startY)
        if x * (n - startY) == (n - y) * startX and startX < x:
            min_len = min(min_len, x**2 + (n - startY)**2 + (n - y)**2 + startX**2)
        # 4. (m - x) : (n - y) = (m - startX) : (n - startY)
        if (m - x) * (n - startY) == (n - y) * (m - startX) and (m - startX) < (m - x):
            min_len = min(min_len, (m - x) ** 2 + (n - startY) ** 2 + (n - y) ** 2 + (m - startX) ** 2)
        # 모서리에 맞을 때
        # 1. 목적 공의 위치를 x = 0에 대칭 -> -x, y
        if y == startY and x < startX:
            pass
        else:
            min_len = min(min_len, (startX + x)**2 + (startY - y)**2)
        
        # 2. 목적 공의 위치를 y = 0에 대칭 -> x, -y
        if x == startX and y < startY:
            pass
        else:
            min_len = min(min_len, (startX - x)**2 + (startY + y)**2)
        
        # 3. 목적 공의 위치를 x = m에 대칭 -> 2m -x, y
        if y == startY and startX < x:
            pass
        else:    
            min_len = min(min_len, (startX - 2*m + x)**2 + (startY - y)**2)
        
        # 4. 목적 공의 위치를 y = n에 대칭 -> x, 2n -y
        if x == startX and startY < y:
            pass
        else:
            min_len = min(min_len, (startX - x)**2 + (startY - 2 * n + y)**2)
        
        answer.append(min_len)        
    
    return answer