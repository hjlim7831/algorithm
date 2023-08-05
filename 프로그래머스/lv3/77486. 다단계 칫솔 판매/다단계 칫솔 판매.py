from collections import defaultdict

graph = defaultdict(str)
res_dict = defaultdict(int)

def dfs(target:str, val:int):
    global graph, res_dict
    up_ben = val // 10
    res_dict[target] += val - up_ben
    if up_ben:
        dfs(graph[target], up_ben)
    
def solution(enroll, referral, seller, amount):
    global graph, sell_dict
    
    for en, ref in zip(enroll, referral):
        graph[en] = ref
    
    for s, a in zip(seller, amount):
        dfs(s, a * 100)
    
    answer = []
    for e in enroll:
        answer.append(res_dict[e])
    
    return answer