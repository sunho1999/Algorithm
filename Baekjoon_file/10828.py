import sys
from collections import deque

def size():
    return (len(stack))

def empty():
    if len(stack) > 0:
        return 0
    else:
        return 1
def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()
def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]
def push(x):
    stack.append(x)

n = int(sys.stdin.readline().rstrip())
stack = deque()
for i in range(n):
    command = sys.stdin.readline().rstrip().split()
    order = command[0]
    if order =="push":
        push(command[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "top":
        print(top())
    elif order == "empty":
        print(empty())