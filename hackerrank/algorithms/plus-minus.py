#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    ratios = [0, 0, 0]
    for num in arr:
        if num > 0:
            ratios[0] += 1
        elif num < 0:
            ratios[1] += 1
        else:
            ratios[2] += 1
    for i, r in enumerate(ratios):
        ratios[i] = r / len(arr)
    for r in ratios:
        print(f"{r:.6f}")
    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
