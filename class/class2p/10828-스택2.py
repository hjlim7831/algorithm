# sys.stdin.readline()을 애용하자..^^
# 리스트라 그런지, append를 하는 경우랑 미리 리스트 크기를 지정해놓고 index로 집어넣는 것이랑 차이가 없는듯?
import sys
stack1 = []

def push(a):
    global stack1
    stack1.append(a)

def pop():
    global stack1
    l = len(stack1)
    if l == 0:
        print(-1)
    else:
        print(stack1[l-1])
        del stack1[l-1]

def size():
    global stack1
    print(len(stack1))

def empty():
    global stack1
    if len(stack1) == 0:
        print(1)
    else:
        print(0)

def top():
    global stack1
    l = len(stack1)
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