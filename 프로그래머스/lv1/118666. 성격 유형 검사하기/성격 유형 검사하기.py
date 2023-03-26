def solution(survey, choices):
    # 0: RT, 1: CF, 2: JM, 3: AN
    score = {"RT": 0, "TR": 0, "CF": 0, "FC": 0, "JM": 0, "MJ": 0, "AN": 0, "NA": 0}
    
    for i in range(len(survey)):
        score[survey[i]] += 4 - choices[i]
    
    personality = ''
    p_type = ["RT", "CF", "JM", "AN"]
    for pt in p_type:
        det = score[pt] - score[pt[::-1]]
        if  det >= 0:
            personality += pt[0]
        else:
            personality += pt[1]    
    
    
    return personality