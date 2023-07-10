import sys
input = sys.stdin.readline


left = list(input().strip())
right = []

num = int(input())

for i in range(num):
    command = input()
    if command[0] == "L":
        if len(left) != 0:
            right.append(left.pop())
    elif command[0] == "D":
        if len(right) != 0:
            left.append(right.pop())
    elif command[0] == "B":
        if len(left) != 0:
            left.pop()
    elif command[0]== "P":
        left.append(command[2])


answer = left + right[::-1]
for i in answer:
    print(i,end="")