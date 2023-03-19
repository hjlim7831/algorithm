def solution(keymap, targets):
    default = 1_000
    min_click = [default for _ in range(26)]
    
    for keys in keymap:
        for i in range(len(keys)):
            idx = ord(keys[i]) - ord("A")
            min_click[idx] = min(min_click[idx], i + 1)
    
    answer = []
    for target in targets:
        no_flag = False
        ans_tmp = 0
        for alp in target:
            idx = ord(alp) - ord("A")
            if min_click[idx] == default:
                no_flag = True
                break
            else:
                ans_tmp += min_click[idx]
        if no_flag:
            answer.append(-1)
        else:
            answer.append(ans_tmp)           
    
    return answer