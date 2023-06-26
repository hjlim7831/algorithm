def solution(arr):
    primes = []
    p_set = set()
    for num in arr:
        primes.append(dict())
        while num != 1:
            for n in range(2, num + 1):
                if num % n == 0:
                    p_set.add(n)
                    if n in primes[-1].keys():
                        primes[-1][n] = primes[-1][n] + 1
                    else:
                        primes[-1][n] = 1
                    num //= n
                    break

    answer = 1
    for num in p_set:
        max_num = 1
        for p_dict in primes:
            if num in p_dict.keys():
                max_num = max(p_dict[num], max_num)
        answer *= num ** max_num
    
    return answer