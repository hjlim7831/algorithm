N = int(input())
card = [i for i in range(1,N+1)]

n = 1
while True:
    l = len(card)
    if l == 1:
        break
    del card[0]
    c = card[0]
    del card[0]
    card.append(c)

print(card[0])

# QUEUE로 푸는 방식.. 이지만 시간 초과..
# collection에서 deque를 가져와 같은 방식으로 풀면 시간초과 없이 해결되는 듯하다.