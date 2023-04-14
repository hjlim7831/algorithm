def solution(targets):
    targets.sort(key=lambda x: (x[0], x[1]))
    # print(targets)
    cnt = 1
    st, ed = targets[0][0], targets[0][1]
    for s, e in targets[1:]:
        # print(st, ed)
        if ed <= s:
            cnt += 1
            st, ed = s, e
        else:
            st, ed = max(s, st), min(e, ed)
            
    return cnt