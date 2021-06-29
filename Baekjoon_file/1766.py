import heapq
import sys

#문제수 , 우선순위 갯수
n , m = map(int,sys.stdin.readline().split())
#간선을 담을 그래프
graph = [[] for _ in range(n+1)]
#indegree
indegree = [0 for _ in range(n+1)]
#heap
heap = []
#결과
result = []
#간선 담기
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

#indegree가 0인 수부터 뽑기
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)

#heap에서 pop하면서 indegree 수정하기(위상정렬)
while heap:
    a = heapq.heappop(heap)
    result.append(a)
    for i in graph[a]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap,i)
for i in result:
    print(i,end=' ')