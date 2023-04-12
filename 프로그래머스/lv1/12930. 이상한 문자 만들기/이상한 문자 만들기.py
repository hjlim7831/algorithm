def solution(s):
    s_list = list(s)
    idx = 0
    for i in range(len(s_list)):
        w = s_list[i]
        if w == " ":
            idx = 0
            continue
        if idx % 2 == 0:
            s_list[i] = w.upper()
        else:
            s_list[i] = w.lower()
        idx += 1
            
    return "".join(s_list)