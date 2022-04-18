cinput = input()
calpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in calpha:
        cinput = cinput.replace(i,'?')

print(len(cinput))