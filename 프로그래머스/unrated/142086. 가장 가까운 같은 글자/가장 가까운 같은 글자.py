def solution(s):
    s_len = len(s)
    answer = []
    alp_dic = {}
    for i in range(s_len):
        w = s[i]
        if w in alp_dic.keys():
            answer.append(i - alp_dic[w])
            alp_dic[w] = i
        else:
            answer.append(-1)
            alp_dic[w] = i
        
            
    
    return answer