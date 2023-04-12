def solution(participant, completion):
    par_dict = {}
    for name in participant:
        if name in par_dict.keys():
            par_dict[name] = par_dict[name] + 1
        else:
            par_dict[name] = 1
    
    for name in completion:
        par_dict[name] = par_dict[name] - 1
        if par_dict[name] == 0:
            del par_dict[name]
    
    for name in par_dict.keys():
        answer = name
    
    return answer