from collections import deque

# 노드 개수, 간선 개수
n,m = map(int,input().split())

# 인접 리스트
matrix = [[] for _ in range(n)]
# 방문 노드 저장
visited = [0 for _ in range(n)]


def dfs(b,save):
    # 시작 노드 체크
    que = deque()
    que.append([b,save])
    visited[b] = 1
    while que:
        node,save = que.popleft()
        # 시작 좌표에서 연결된 간선 탐색
        for i,save_node in matrix[node]:
            # 방문한 좌표가 방문하지 않은 좌표일 때
            if visited[i] == 0:
                # 인접리스트의 간선 노드와 현재 간선노드가 같을 때 que에 추가
                if matrix[i][save_node] == matrix[node][save]:
                    que.append(i)
            # 방문한 좌표가 방문했던 좌표일 때
            if visited[i] != 0:



save = 1
for i in range(m):
    a,b = map(int,input().split())
    matrix[a].append([b,save])
    matrix[b].append([a.save])
    save +=1
    dfs(b)
print(matrix)


