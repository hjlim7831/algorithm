N = int(input())

n = 666
i = 0
while True:
    numl = list(map(int,str(n)))
    for j in range(len(numl)-2):
        if numl[j:j+3] == [6,6,6]:
            # print(n)
            i += 1
            break
    if i == N:
        print(n)
        break
    n += 1