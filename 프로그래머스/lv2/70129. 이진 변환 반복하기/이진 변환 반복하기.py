def solution(s):
    cnt0, cnt = 0, 0
    # for _ in range(3):
    while s != "1":
        cnt0 += s.count("0")
        s = s.replace("0", "")
        cnt += 1
        s = bin(len(s))[2:]
            
    return [cnt, cnt0]