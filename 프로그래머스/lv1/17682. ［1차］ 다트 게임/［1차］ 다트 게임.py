def solution(dartResult):
    scores = []
    score = ""
    dartResult = dartResult.replace("10", "a")
    for c in dartResult:
        if c.isdigit() or c == "a":
            scores.append(score)
            score = c
        else:
            score += c
    scores.append(score)
    print(scores)
    scores_num = []
    for i in range(1, 4):
        dart = scores[i]
        if dart[0] == "a":
            score = 10
        else:
            score = int(dart[0])
        
        if dart[1] == "S":
            score = score
        elif dart[1] == "D":
            score = score * score
        elif dart[1] == "T":
            score = score * score * score
        
        if len(dart) == 3:
            if dart[2] == "#":
                score = -score
            elif dart[2] == "*":
                score = score * 2
                if scores_num:
                    scores_num[-1] = scores_num[-1] * 2
        scores_num.append(score)
            
    return sum(scores_num)