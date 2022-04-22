# x: 5kg, y: 3kg
# x + y 
# 5*x + 3*y = N
# (N - 3y)/5, y
N = int(input())

y = 0
while True:
    if (N-3*y)/5 == int((N-3*y)/5):
        print(int((N-3*y)/5)+y)
        break
    
    if (N-3*y)/5 < 0:
        print(-1)
        break

    y += 1