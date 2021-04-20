import sys
import heapq
inf = sys.maxsize

#정점 수 , 간선 수
v,e = map(int,sys.stdin.readline().split())
#시작 정점
k = int(input())
#가중치 테이블
dp = [inf]*(v+1)
#힙
heap = []
#graph
graph = [[]for _ in range(v+1)]

for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    #가중치 저장
    graph[a].append((c,b))

def dijkstar(start):
    dp[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        wei,go = heapq.heappop(heap)
        if dp[go] < wei :
            continue
        else:
            for i,j in graph[go]:
                next_wei = wei + i
                if dp[j] > next_wei:
                    dp[j] = next_wei
                    heapq.heappush(heap,(next_wei,j))
dijkstar(k)


for i in range(1,v+1):
    if dp[i] == inf:
        print("INF")
    else:
        print(dp[i])
