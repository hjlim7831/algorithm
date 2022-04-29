import sys

deque1, l = [], 0

def push_front(x):
    global deque1, l
    deque1.insert(0,x)
    l += 1

def push_back(x):
    global deque1, l
    deque1.insert(l,x)
    l += 1

def pop_front():
    global deque1, l
    if l == 0:
        print(-1)
    else:
        print(deque1[0])
        del deque1[0]
        l -= 1

def pop_back():
    global deque1, l
    if l == 0:
        print(-1)
    else:
        print(deque1[l-1])
        del deque1[l-1]
        l -= 1

def size():
    global l
    print(l)

def empty():
    global l
    if l == 0:
        print(1)
    else:
        print(0)

def front():
    global deque1, l
    if l == 0:
        print(-1)
    else:
        print(deque1[0])

def back():
    global deque1, l
    if l == 0:
        print(-1)
    else:
        print(deque1[l-1])

N = int(sys.stdin.readline())
for i in range(N):
    comm = sys.stdin.readline().strip().split()
    if comm[0] == "push_front":
        push_front(int(comm[1]))
    elif comm[0] == "push_back":
        push_back(int(comm[1]))
    elif comm[0] == "pop_front":
        pop_front()
    elif comm[0] == "pop_back":
        pop_back()
    elif comm[0] == "size":
        size()
    elif comm[0] == "empty":
        empty()
    elif comm[0] == "front":
        front()
    elif comm[0] == "back":
        back()