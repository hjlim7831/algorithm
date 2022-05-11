def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

N = int(input())
num = fact(N)
#print(num)
ans = 0
while True:
    if num%10 == 0:
        num = num//10
        ans += 1
    else:
        break
print(ans)