from collections import deque

num = int(input())
card_stack = [i for i in range(num,0,-1)]
card_stack = deque(card_stack)

while(len(card_stack)!=1):
    card_stack.pop()
    card_stack.insert(0,card_stack.pop())
print(card_stack[0])