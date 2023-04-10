def solution(name, yearning, photo):
    missing = {}
    for i in range(len(name)):
        missing[name[i]] = yearning[i]
    
    score = []
    
    for people in photo:
        tmp_score = 0
        for person in people:
            if person in missing.keys():
                tmp_score += missing[person]
        score.append(tmp_score)
    return score