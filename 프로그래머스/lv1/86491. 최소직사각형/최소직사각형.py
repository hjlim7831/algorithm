def solution(sizes):
    xlen, ylen = 0, 0
    for x, y in sizes:
        if x > y:
            y, x = x, y
        xlen = max(xlen, x)
        ylen = max(ylen, y)
    return xlen * ylen