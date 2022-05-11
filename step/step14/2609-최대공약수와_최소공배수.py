a, b = map(int,input().split())
axb = a*b

tt = min(a,b)
if tt == 1:
    print(1)
    print(max(a,b))
else:
    G = 1
    while True:
        tt = min(a,b)
        for i in range(2,tt+1):
            if a%i == 0 and b%i == 0:
                G *= i
                a = a//i
                b = b//i
                break
        if i == tt or a == 1 or b == 1:
            break

    print(G)
    print(axb//G)

"""
아.. 정말 많이 틀렸다 ㅋㅋㅋㅋㅋㅋ
아무래도 테스트를 할 때에는, 크고 복잡한 값도 물론 해야하지만
기본적으로 제일 작은 값이 되는지를 확인해봐야겠다.. 그쪽에서 종종 틀리는 듯.
"""