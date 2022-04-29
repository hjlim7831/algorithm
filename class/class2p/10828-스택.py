# sys.stdin.readline()을 애용하자..^^

import sys

stack1 = [0]*10000
l = 0

def push(a):
    global stack1, l
    stack1[l] = a
    l += 1

def pop():
    global stack1, l
    if l == 0:
        print(-1)
    else:
        print(stack1[l-1])
        stack1[l-1] = 0
        l -= 1

def size():
    global stack1, l
    print(l)

def empty():
    global stack1, l
    if l == 0:
        print(1)
    else:
        print(0)

def top():
    global stack1, l
    if l == 0:
        print(-1)
    else:
        print(stack1[l-1])

N = int(sys.stdin.readline())

for i in range(N):
    comm = sys.stdin.readline().strip()
    if comm == "pop":
        pop()
    elif comm == "size":
        size()
    elif comm == "empty":
        empty()
    elif comm == "top":
        top()
    elif comm.split()[0] == "push":
        a = int(comm.split()[1])
        push(a)