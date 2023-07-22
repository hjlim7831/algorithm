from itertools import permutations

def chk_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    prime_numbers = set()    
    for i in range(1, len(numbers)+1):
        for num_list in permutations(numbers, i):
            num = int("".join(num_list))
            if chk_prime(num):
                prime_numbers.add(num)
    return len(prime_numbers)