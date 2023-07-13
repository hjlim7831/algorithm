def solution(cards):
    len_groups = [0]
    not_visited = set(range(1, len(cards)+1))
    while not_visited:
        cnt = 1
        val = not_visited.pop()
        nex = cards[val-1]
        while nex in not_visited:
            not_visited.remove(nex)
            cnt += 1
            nex = cards[nex-1]
        len_groups.append(cnt)
    len_groups.sort(reverse=True)
    return len_groups[0] * len_groups[1]
