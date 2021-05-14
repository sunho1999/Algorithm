import heapq
import sys

inf = 987654321

def dijkstar(start,end,matrix):
    que = []
    visited = [inf]*(n+1)
    visited[start] = 0
    heapq.heappush(que,[start,0])
    while que:
        pos ,cost = heapq.heappop(que)

        for p,c in matrix[pos]:
            c = c + cost
            if visited[p] > c:
                visited[p] = c
                heapq.heappush(que,[p,c])

    print(visited[end])

#노드 수
n = int(sys.stdin.readline())
#간선 갯수
m = int(sys.stdin.readline())
#각 노드의 간선 값 저장
matrix = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    matrix[a].append((b,c))

#시작 노드 , 도착 노드
start,end = map(int,input().split())

dijkstar(start,end,matrix)