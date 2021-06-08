n = int(input()) #노드 개수
parent_num = list(map(int,input().split())) #부모노드 체크
delte_node = int(input()) #지울 노드

graph = [[False] * n for _ in range(n)]
visited = [False] * n
cnt = 0
#재귀를 통해 부모 노드에서 자식 노드로 들어가면서 visit으로 노드방문 체크 후 리프노드로 도착할때마다 카운트 증가
def dfs(root):
    global cnt
    check = False
    visited[root] = True
    for i in range(n):
        if visited[i] == False and graph[root][i]:
            check = True
            dfs(i)
    if not check:
        cnt += 1

#인접행렬로 루트를 제외한 나머지 노드들은 체크
for i in range(n):
    if parent_num[i] != -1:
        graph[i][parent_num[i]] = True
        graph[parent_num[i]][i] = True
    else:
        root = i
#자를 노드와 그 밑에 자식 노드 제거
for i in range(n):
    graph[i][delte_node] = False
    graph[delte_node][i] = False

dfs(root)

if delte_node == root:
    print(0)
else:
    print(cnt)