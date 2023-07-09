def solution(N, number):
    ans = []
    ans.append(set())
    for n in range(1, 9):
        nums_n = set()
        nums_n.add(int(str(N)*n))
        for i in range(1, n//2 + 1):
            for t1 in ans[i]:
                for t2 in ans[n-i]:
                    nums_n.add(t1 + t2)
                    nums_n.add(t1 - t2)
                    nums_n.add(t2 - t1)
                    nums_n.add(t1 * t2)
                    if t2 != 0:
                        nums_n.add(t1 // t2)
                    if t1 != 0:
                        nums_n.add(t2 // t1)
        if number in nums_n:
            return n
        ans.append(nums_n)        
    
    return -1