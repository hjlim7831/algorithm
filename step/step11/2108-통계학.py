N = int(input())

num = [0]*N
for i in range(N):
    num[i] = int(input())

m1 = 0
for i in range(N):
    m1 += num[i]
m1 = m1/N

num.sort()
m2 = num[int((N-1)/2)]

m4 = max(num) - min(num)

minm = min(num)
count = [0]*m4
for i in range(N):
    ind = num[i] - minm
    count[ind] += 1
maxc = max(count)



print(f"{m1:.0f}")
print(m2)

print(m4)