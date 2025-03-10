import sys
from collections import deque

n = int(input())
que = deque()
que.append([n])
ans = []

while que:
    # print(que)
    a = que.popleft()
    x = a[0]
    if x == 1:
        ans = a
        break

    if x % 3 == 0:
        que.append([x//3]+a)

    if x % 2 == 0:
        que.append([x//2]+a)

    que.append([x-1]+a)

print(len(ans) - 1)
print(*ans[::-1])