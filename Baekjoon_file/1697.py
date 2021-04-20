import sys
from collections import deque


def bfs(V):
    q = deque()
    q.append(V)
    while q:
        a = q.popleft()
        if a == K:
            print(dust[a])
            break
        if 0<= a-1 <= max and dust[a-1] ==0:
            dust[a-1] = dust[a]+1
            q.append(a-1)
        if 0 <= a + 1 <= max and dust[a + 1] == 0:
            dust[a + 1] = dust[a] + 1
            q.append(a + 1)
        if 0 <= a * 2 <= max and dust[a * 2] == 0:
            dust[a * 2] = dust[a] + 1
            q.append(a * 2)


N, K = map(int,sys.stdin.readline().split())
max = 100000+1
dust = [0]*(max+1)
bfs(N)

