def solution(arr):
    numbers, ops = list(map(int, arr[::2])), arr[1::2]
    ln = len(numbers)
    
    sum_min, sum_max = {}, {}
    for idx, num in enumerate(numbers):
        sum_min[(idx, idx)] = num
        sum_max[(idx, idx)] = num
    
    for d in range(1, ln+1):
        for ed in range(d, ln):
            st = ed - d
            key = (st, ed)
            for mid in range(st, ed):
                op = ops[mid]
                if op == "+":
                    min_val = sum_min[(st, mid)] + sum_min[(mid+1, ed)]
                    max_val = sum_max[(st, mid)] + sum_max[(mid+1, ed)]
                    
                    if key in sum_min.keys():
                        sum_min[key] = min(sum_min[key], min_val)
                        sum_max[key] = max(sum_max[key], max_val)
                    else:
                        sum_min[key] = min_val
                        sum_max[key] = max_val
                else:
                    min_val = sum_min[(st, mid)] - sum_max[(mid+1, ed)]
                    max_val = sum_max[(st, mid)] - sum_min[(mid+1, ed)]
                    if key in sum_min.keys():
                        sum_min[key] = min(sum_min[key], min_val)
                        sum_max[key] = max(sum_max[key], max_val)
                    else:
                        sum_min[key] = min_val
                        sum_max[key] = max_val
    return sum_max[(0, ln-1)]