init_list = [i for i in range(101)]

def find_set(a):
    if init_list[a] != a:
        init_list[a] = find_set(init_list[a])
    return init_list[a]

# b를 a 영역으로 넣기
def union(a, b):
    init_list[b] = a


def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    answer = 0
    cnt, idx = 0, 0
    while cnt < n-1:
        st, ed, cost = costs[idx]
        st_f, ed_f = find_set(st), find_set(ed)
        if st_f != ed_f:
            union(st_f, ed_f)
            answer += cost
            cnt += 1
        idx += 1
        # print(init_list[:n])
        
    return answer