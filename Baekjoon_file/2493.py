n = int(input())

top_list = list(map(int,input().split()))
answer = []
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] < top_list[i]:
            stack.pop()
        elif stack[-1][1] > top_list[i]:
            answer.append(stack[-1][0]+1)
            break
    if not stack :
        answer.append(0)
    stack.append([i,top_list[i]])


print(" ".join(map(str, answer)))