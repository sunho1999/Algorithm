import  sys
from collections import deque
input = sys.stdin.readline

def CtoI(target):
    if target.isupper():
        return ord(target) - ord('A')
    else:
        return ord(target) - ord('a') + 26

def edmonds_karp(source,sink):
    totalflow = 0

    while True:
        visited  = [-1] * max_n # 노드의 갯수만큼 초기 방문 노드를 만듬.
        if bfs(source,sink,visited): # bfs탐색 시작
            break

        minFlow = 10000000000 # 무한대, 임의상 큰 숫자로 넣음

        i = sink # i 는 sink로 초기화 .
        while i != source: # i가 source가 같아질 떄 까지 반복문 진행
            minFlow = min(minFlow, capacity[visited[i]][i] - flow[visited[i]][i]) # minFlow와 sink를 가기위한 이전 prev 인접 노드의 수용량과
            # prev 인접 노드의 flow를 뺀 값을 비교
            i = visited[i] # visted[i] 즉, sink를 가기 전의 prev node를 i 값으로 바꿈
        i = sink
        while i != source:
            flow[visited[i]][i] += minFlow # 양의 간선에 대해선 minFlow를 더함
            flow[i][visited[i]] -= minFlow # 음의 간선에 대해선 minFlow를 뺌
            i = visited[i] # visted[i] 즉, sink를 가기 전의 prev node를 i 값으로 바꿈
        totalflow += minFlow
    return totalflow

def bfs(source,sink,visited):
    que = deque() # 연산편의를 위해 python deque사용.
    que.append(source)

    while que and visited[sink] == -1: # que에 인자값이 있고, 끝지점에 도착하지 않았을 떄 whlie 진행
        start = que.popleft() # que popleft 진행
        for end in adj_list[start]: # start노드에서의 인접한 node들 탐색 ( adjancecy matrix 사용)
            if capacity[start][end] - flow[start][end] > 0 and visited[end] == -1: # 수용력 - 유량 을 뺏을 때 0보다 크고, 인접 노드들이 방문하지 않았을 때 탐색 진행.
                que.append(end) # 탐색한 인접 노드들을 que에 추가
                visited[end] = start # visited에 0 또는 1이 아닌, 추 후 flow 계산을 위해 인접노드를 접근하기위한 prev 노드를 visited 인자값으로 사용.

                if end == sink: # 인접 노드가 sink(도착지점) 이면 break
                    break
    if visited[sink] == -1:
        return  True
    else:
        return False

n  = int(input())
max_n  = 52 #노드의 갯수
flow = [[0 for _ in range(max_n)]  for _ in range(max_n)]  # 유량
capacity = [[0 for _ in range(max_n)] for _ in range(max_n)] # 수용량
adj_list = [[] for _ in range(max_n)]

for i in range(n):
    start, end ,c = input().strip().split() # 출발, 도착
    print(start,end,c)

    start = CtoI(start)
    end = CtoI(end)
    capacity[start][end] = int(c) # 수용량을 둘다 추가함.
    capacity[end][start] = int(c)

    adj_list[start].append(end)  #adjancency matrix를 사용하여 vertex 사이들끼리의 인접관계를 저장함
    adj_list[start].append(start)

source = CtoI("A") # 시작지점
sink = CtoI("Z") # 도착지점

a = edmonds_karp(source,sink)

print(a)