n, m = map(int,input().split())

n1, m1 = n, m
num_over = 1
num_under = 1
for i in range(m):
    num_over *= n1
    num_under *= m1
    n1 -= 1
    m1 -= 1


num = num_over//num_under
#print(num)

ans = 0
while True:
    if num%10 == 0:
        ans += 1
        num = num//10
    else:
        break
print(ans)