def solution(today, terms, privacies):
    term_dic = {}
    for term in terms:
        typ, mon = term.split()
        term_dic[typ] = int(mon)
    
    today_num = int(today.replace(".", ""))
    
    answer = []
    ans_num = 1
    for privacy in privacies:
        dat, typ = privacy.split()
        mon = term_dic[typ]
        yr, mo, dy = map(int, dat.split("."))
        mo += mon
        while mo > 12:
            yr += 1
            mo -= 12
        
        priv_num = yr*10**4 + mo*100 + dy
        # print(priv_num)
        if priv_num <= today_num:
            answer.append(ans_num)
        ans_num += 1
            
        
    
    
    return answer