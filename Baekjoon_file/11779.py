import heapq
import sys
sys.setrecursionlimit(100000000)
n = int(input())
m = int(input())
inf = 1e9

linked_list = [[] for _ in range(n+1)]
distance = [inf]*(n+1)
for i in range(m):
    v1,v2,e = map(int,sys.stdin.readline().split())
    linked_list[v1].append([v2,e])

start,end = map(int,sys.stdin.readline().split())

city = [[] for _ in range(n+1)]
city[start].append(start)


def dijkstra(start):
    que = []
    heapq.heappush(que,[start,0])
    distance[start] = 0
    while que:
        now, dist = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for i in linked_list[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que,(i[0],cost))
                city[i[0]] = []
                for j in city[now]:
                    city[i[0]].append(j)
                city[i[0]].append(i[0])

dijkstra(start)


print(distance[end])
print(len(city[end]))
print(' '.join(map(str,city[end])))

