#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    num_gcd = b[0]
    for i in range(1, len(b)):
        num_gcd = math.gcd(num_gcd, b[i])
    cand = set()
    for i in range(1, int(num_gcd**0.5)+1):
        if num_gcd % i == 0:
            cand.add(i)
            cand.add(num_gcd // i)
    
    cnt = 0
    for c in cand:
        for an in a:
            if c % an != 0:
                break
        else:
            cnt += 1
    return cnt
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
