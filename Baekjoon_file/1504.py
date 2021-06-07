import heapq
import sys
inf = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 방향성 없는 그래프이므로 x, y일 때와 y, x일 때 모두 추가
for _ in range(e):
    x, y, cost = map(int,sys.stdin.readline().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))


def dijkstra(start):
    distance =[inf]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance

v1,v2 = map(int,input().split())
original_distance = dijkstra(1)

v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)
v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)

if result < inf:
    print(result)
else:
    print(-1)