from itertools import combinations
import collections
from bisect import bisect_left

def solution(info, query):
    db = collections.defaultdict(list)
    for i in info:
        isplit = i.split()
        score = int(isplit[-1])
        condition = isplit[:-1]
        db["----"].append(score)
        db["".join(condition)].append(score)
        
        for n in range(1, 4):
            for sel in combinations([0, 1, 2, 3], n):
                key = ""
                for idx in [0, 1, 2, 3]:
                    if idx in sel:
                        key += condition[idx]
                    else:
                        key += "-"
                db[key].append(score)
    
    for k in db:
        db[k].sort()

    answer = []    
    for q in query:
        q = q.replace("and ", "")
        q = q.split()
        target_key = "".join(q[:-1])
        target_score = int(q[-1])
        count = 0
        if target_key in db:
            target_list = db[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)
    
    
    return answer