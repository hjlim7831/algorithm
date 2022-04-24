def hanoi(t1, t2, n):
    t3 = 6 - t1 - t2
    if n == 1:
        print(t1, t2)
        return
    else:
        hanoi(t1, t3, n-1)
        print(t1, t2)
        hanoi(t3, t2, n-1)

N = int(input())
print(2**N-1)
hanoi(1, 3, N)

"""
음... 아무래도 내가 에러가 났던 것은 n=1일 때를 정의하지 않았기 때문인듯?
왜 recursion error가 떴는지 알겠다 ㅋㅋㅋㅋ
재귀 문제를 풀 때에는 점화식과 같이 접근하면 되니까, 규칙이 헷갈릴 때에는 숫자가 작은 경우부터 직접 나열해보고, 거기서 규칙성을 찾아보자!
"""