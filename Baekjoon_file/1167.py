from collections import deque
import sys
n = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]

for _ in range(n):
    c = list(map(int,sys.stdin.readline().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))

def bfs(start):
    visit = [-1]*(n+1)
    que = deque()
    que.append(start)
    visit[start] = 0
    max = [0,0]
    while que:
        a = que.popleft()
        for j,k in graph[a]:
            if visit[j] == -1:
                visit[j] = visit[a] + k
                que.append(j)
            if max[0] < visit[j]:
                max =  visit[j],j

    return max
t,y = bfs(1)
t,y = bfs(y)

print(t)
