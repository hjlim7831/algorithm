import math
import time
def sosu(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

sosu_list = []

while True:
    sosu_list.clear()
    n = int(input())
    start = time.time()
    if n == 0:
        break
    
    if n == 1:
        print(1)
        
    if n > 1:
        for i in range(n + 1, 2 * n):
            if sosu(i):
                sosu_list.append(i)
        print(len(sosu_list))
        print("time: ",time.time() - start)