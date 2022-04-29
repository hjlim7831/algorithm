import sys

queue1 = []
l = 0
def push(a):
    global queue1, l
    queue1.append(a)
    l += 1

def pop():
    global queue1, l
    if l == 0:
        print(-1)
    else:
        print(queue1[0])
        del queue1[0]
        l -= 1

def size():
    global queue1, l
    print(l)

def empty():
    global queue1, l
    if l == 0:
        print(1)
    else:
        print(0)

def front():
    global queue1, l
    if l == 0:
        print(-1)
    else:
        print(queue1[0])

def back():
    global queue1, l
    if l == 0:
        print(-1)
    else:
        print(queue1[l-1])

N = int(sys.stdin.readline())
for i in range(N):
    comm = sys.stdin.readline().strip()
    if comm == "pop":
        pop()
    elif comm == "size":
        size()
    elif comm == "empty":
        empty()
    elif comm == "front":
        front()
    elif comm == "back":
        back()
    elif comm.split()[0] == "push":
        a = int(comm.split()[1])
        push(a)
