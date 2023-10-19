import sys
import heapq
n, d = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(d+1)]

for i in range(d):
    graph[i].append((i+1, 1))

for i in range(n):
    start, end, length = map(int, sys.stdin.readline().split())
    if end > d:
        continue
    graph[start].append((end,length))

INF = 10e9
distance = [INF]*(d+1)
distance[0] = 0
que = []
heapq.heappush(que, (0, 0))

while que:
    d, now = heapq.heappop(que)
    if distance[now] < d:
        continue
    for x in graph[now]:
        cost = d + x[1]

        if distance[x[0]] > cost:
            distance[x[0]] = cost
            heapq.heappush(que, (cost, x[0]))
print(distance[d])



