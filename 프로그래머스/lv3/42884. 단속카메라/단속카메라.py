def solution(routes):
    routes.sort(key=lambda x:(x[0], -x[1]))
    cnt = 1
    st, ed = -30_000, 30_000
    lr = len(routes)
    for rst, red in routes:
        st = max(st, rst)
        ed = min(ed, red)
        if st > ed:
            cnt += 1
            st, ed = rst, red
    return cnt