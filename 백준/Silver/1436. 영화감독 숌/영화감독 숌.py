import sys
input = sys.stdin.readline

N = int(input())

titles_set = set()

def make_title(res:str, idx:int):
    global titles_set
    titles_set.add(int(res))
    if idx == 4:
        return

    for n in range(10):
        make_title(res+str(n), idx+1)
        make_title(str(n)+res, idx+1)

make_title("666", 0)

titles = list(titles_set)
titles.sort()
print(titles[N-1])