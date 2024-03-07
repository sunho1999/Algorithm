import heapq

n,m = map(int,input().split())
INF = int(1e9)
linked_list = [[] for _ in range(n+1)]

for i in range(m):
    node1,node2,cost = map(int,input().split())
    linked_list[node1].append((node2,cost))
    linked_list[node2].append((node1,cost))

distance = [INF] * (n+1)
# print(distance)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in linked_list[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
# print(distance)
if distance[n] == INF:
    print(-1)
else:
    print(distance[n])

