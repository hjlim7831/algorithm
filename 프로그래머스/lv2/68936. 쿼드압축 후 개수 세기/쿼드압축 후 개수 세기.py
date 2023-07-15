def div(arr, sr, sc, n):
    if n == 2:
        res = [0, 0]
        for r in range(sr, sr+2):
            for c in range(sc, sc+2):
                res[arr[r][c]] += 1
        if res[0] == 4:
            return [1, 0]
        elif res[1] == 4:
            return [0, 1]
        else:
            return res
    
    nn = n // 2
    res = [0, 0]
    for r in [sr, sr+nn]:
        for c in [sc, sc+nn]:
            tmp = div(arr, r, c, nn)
            res[0] += tmp[0]
            res[1] += tmp[1]
    if res[0] == 4 and res[1] == 0:
        return [1, 0]
    elif res[1] == 4 and res[0] == 0:
        return [0, 1]
    else:
        return res
    
def solution(arr):
    answer = div(arr, 0, 0, len(arr))
    return answer


