
def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0
    len1, len2 = len(cards1), len(cards2)
    no_flag = False
    for word in goal:
        if idx1 < len1:
            if cards1[idx1] == word:
                idx1 += 1
                continue
        if idx2 < len2:
            if cards2[idx2] == word:
                idx2 += 1
                continue
        no_flag = True
        break
    if no_flag:
        answer = "No"
    else:
        answer = "Yes"
    
    return answer