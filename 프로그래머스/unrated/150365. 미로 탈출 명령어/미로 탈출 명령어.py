def solution(n, m, x, y, r, c, k):
    # 순서 : d, l, r, u
    directs = [(-1, 0, "u"), (0, 1, "r"), (0, -1, "l"), (1, 0, "d")]
    
    stack = [(x, y, 0, "")]
    
    if (k - abs(x - r) - abs(y - c)) % 2 != 0:
        return "impossible"
    
    complete = False
    while stack:
        # print(stack)
        cx, cy, ccnt, path = stack.pop()
        if abs(cx - r) + abs(cy - c) > (k - ccnt):
            continue
        if cx == r and cy == c and ccnt == k:
            return path
        for dx, dy, d in directs:
            nx = dx + cx
            ny = dy + cy
            if nx < 1 or nx > n or ny < 1 or ny > m:
                continue
            stack.append((nx, ny, ccnt + 1, path + d))
    
    return "impossible"
