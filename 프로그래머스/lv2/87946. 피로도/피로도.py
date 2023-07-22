cnt = 0

def travel(k, dungeons, visited):
    global cnt    
    cnt = max(cnt, bin(visited).count("1"))
    
    for i in range(len(dungeons)):
        idx = 1 << i
        if visited & idx or dungeons[i][0] > k:
            continue
        travel(k-dungeons[i][1], dungeons, visited | idx)


def solution(k, dungeons):
    global cnt
    visited = 0
    travel(k, dungeons, visited)
    
    return cnt