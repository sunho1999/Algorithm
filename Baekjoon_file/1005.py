import sys
from collections import deque

def topologicalSort():
    for _ in range(n):
        if not que:
            return
        #que에서 indegree 0인 노드 추출
        a = que.popleft()
        #indegree가 0인 노드가 향하는 노드 탐색후 그 노드의 value추가하기
        #추가적으로 탐색하면서 인접 노드 indegree -1하기
        for x in matrix[a]:
            answer[x] = max(answer[x], answer[a]+value_node[x])
            indegree[x] -=1

            if indegree[x] == 0:
                que.append(x)

    return
testcase = int(input())
for i in range(testcase):
    #그래프 노드 갯수, 건설규칙갯수
    n,k = map(int,input().split())
    #진입 차수
    indegree = [0]*(n+1)
    #답 추출 리스트
    answer = [0]*(n+1)
    #인접리스트
    matrix = [[] for _ in range(n+1)]
    #각 노드의 소요시간
    value_node = [0]
    value_node = value_node + list(map(int,sys.stdin.readline().split()))
    #인접리스트 만들기
    for i in range(k):
        a,b = map(int,sys.stdin.readline().split())
        matrix[a].append(b)
        indegree[b] +=1
    #종점
    end = int(input())

    que = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            answer[i] = value_node[i]
            que.append(i)

    topologicalSort()

    print(answer[end])





