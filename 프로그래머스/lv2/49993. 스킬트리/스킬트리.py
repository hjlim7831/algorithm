import collections


def solution(skill, skill_trees):
    adj_list = collections.defaultdict(str)
        
    for i in range(len(skill)-1):
        st, ed = skill[i], skill[i+1]
        adj_list[st] = ed
    
    answer = 0
    for skill_tree in skill_trees:
        # print("skill tree: ", skill_tree)
        cnt_list = collections.defaultdict(int)
        for v in adj_list.values():
            cnt_list[v] = 1
        flag = True
        for sk in skill_tree:
            if cnt_list[sk] != 0:
                flag = False
                break
            ed = adj_list[sk]
            if ed:
                cnt_list[ed] -= 1
        if flag:
            answer += 1
            

    return answer