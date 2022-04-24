import time

def draw_stars(n):
  if n==1:
    return ['*']

  Stars=draw_stars(n//3)
  L=[]

  for star in Stars:
    L.append(star*3)
  for star in Stars:
    L.append(star+' '*(n//3)+star)
  for star in Stars:
    L.append(star*3)

  return L

N=int(input())
start = time.time()
print('\n'.join(draw_stars(N)))
print(time.time() - start)

"""
이 분은 맨 밑바닥부터 한 단계씩 올라가는 방식으로 생각했다..
이렇게 생각할 수도 있구나..??
"""