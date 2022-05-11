def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

N = int(input())
ring = list(map(int,input().split()))

B = ring[0]
for i in range(1,N):
    ab_gcd = gcd(ring[i],B)
    print(f'{B//ab_gcd}/{ring[i]//ab_gcd}')