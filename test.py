N = int(input())
n = 0
nf, nz = N//10, N%10
new_num = N
while True:
    nsum = nf + nz
    new_num = nz*10 + nsum%10
    nf, nz = nz, nsum%10
    n += 1
    if N == new_num:
        break

print(n)