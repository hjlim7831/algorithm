def solution(clothes):
    c_dict = {}
    for c_name, c_typ in clothes:
        if c_typ in c_dict.keys():
            c_dict[c_typ].append(c_name)
        else:
            c_dict[c_typ] = [c_name]
    
    answer = 1
    for key in c_dict.keys():
        answer *= len(c_dict[key]) + 1
    answer -= 1
        
    return answer