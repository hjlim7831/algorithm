N = int(input())
card = [i for i in range(1,N+1)]

n = 1
while True:
    l = len(card)
    if l == 1:
        break
    pcard = card
    card = card[n::2]
    n = (len(pcard)+n)%2
#    print(card)

print(card[0])