#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hr, ti = int(s[:2]), s[-2:]
    if ti == "PM":
        return f"{(hr%12+12):02d}"+s[2:-2]
    else:
        return f"{hr%12:02d}"+s[2:-2]
        
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
