
def solution(s):
    s_len = len(s)
    cnt = 0
    x = ""
    for idx in range(s_len):
        print(x)
        if x == "":
            x = s[idx]
            x_cnt = 0
            nx_cnt = 0
        if x == s[idx]:
            x_cnt += 1
        else:
            nx_cnt += 1
        if x_cnt == nx_cnt:
            cnt += 1
            x = ""
    if x != "":
        cnt += 1
    
    
    return cnt

