def bn(n):
    return int(n*(n+1)/2)

X = int(input())

n = 0
while True:
    if bn(n) < X <= bn(n+1):
#        print(n)
        break
    n += 1

tot = n + 2
d = X - bn(n)

if tot%2 == 0:
    print(f'{tot-d}/{d}')
else:
    print(f'{d}/{tot-d}')