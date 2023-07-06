def solution(elements):
    numbers = set(elements)
    numbers.add(sum(elements))
    le = len(elements)
    acc_nums = elements[:]
    for d in range(1, le-1):
        for base_idx in range(le):
            idx = (d + base_idx) % le
            acc_nums[base_idx] = acc_nums[base_idx] + elements[idx]
            numbers.add(acc_nums[base_idx])
    # print(numbers)
    
    return len(numbers)