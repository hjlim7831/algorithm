stri = input()
stri_up = stri.upper()
#print(stri_up)
alp = [0 for i in range(26)]

for st in stri_up:
    ind = ord(st)-65
#    print(ind)
    alp[ind] += 1

maxn = max(alp)
ind1 = alp.index(maxn)
del alp[ind1]

try:
    ind = alp.index(maxn)
    print("?")
except ValueError:
    print(chr(ind1+65))
