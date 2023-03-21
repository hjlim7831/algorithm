def solution(s, skip, index):
    # index 만큼 나가면서 하나씩 set에 있는지 확인
    # 있으면 +1
    skip_set = set(map(str, skip))
    print(skip_set)
    chg_dic = {}
    for i in range(26):
        alp = chr(i + ord("a"))
        cnt = 0
        idx = i
        chk_alp = chr(idx + ord("a"))
        while cnt < index or chk_alp in skip_set:
            idx = (idx + 1) % 26
            chk_alp = chr(idx + ord("a"))
            if chk_alp not in skip_set:
                cnt += 1
        chg_dic[alp] = chr(idx + ord("a"))
    answer = ''
    for w in s:
        answer += chg_dic[w]
    
    return answer