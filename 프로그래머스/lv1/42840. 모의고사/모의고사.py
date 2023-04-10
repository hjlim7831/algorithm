def solution(answers):
    patterns = []
    patterns.append([1,2,3,4,5])
    patterns.append([2,1,2,3,2,4,2,5])
    patterns.append([3,3,1,1,2,2,4,4,5,5])
    
    result = []
    
    for i in range(3):
        pattern = patterns[i]
        p_len = len(pattern)
        score = 0
        for j in range(len(answers)):
            answer = answers[j]
            guess = pattern[j % p_len]
            if answer == guess:
                score += 1
        result.append((score, i + 1))
    result.sort(key=lambda x:x[0], reverse=True)
    
    most = []
    most.append(result[0][1])
    for i in range(1, 3):
        if result[i][0] == result[0][0]:
            most.append(result[i][1])
                
    return most