a = [0 for i in range(10)]
for i in range(10):
    a[i] = int(input())
b = [aa%42 for aa in a]
c = [0 for i in range(42)]
for i in range(10):
    c[b[i]] = 1
print(sum(c))
