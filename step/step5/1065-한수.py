N = int(input())
han = [i for i in range(1,10)]
for ii in range(1,10):
    for d in range(-9,10):
        an = ii + d
        hn = str(ii)
        for k in range(2):
            if not 0 <= an <= 9:
                break
            else:
                hn = hn + str(an)
                an = an + d
                han.append(int(hn))
#                print("hn",hn, "d",d)
lis = [i for i in han if i<=N]
print(len(lis))