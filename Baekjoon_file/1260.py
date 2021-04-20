N,M,V = map(int,input().split())

matrix = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    #이중리스트로 연결 노드 표현
    matrix[a][b] = matrix[b][a] =1
    visited = [0]*(N+1)

def bfs(V):
    que = []
    que.append(V)
    visited[V] = 0
    while que:
        V = que.pop(0)
        print(V,end=" ")
        for i in range(1,N+1):
            if  matrix[V][i] == 1 and visited[i] == 1:
                que.append(i)
                visited[i] = 0


def dfs(V):
    #시작 지점 저장
    visited[V] = 1
    print(V,end=" ")
    for i in range(1,N+1):
        if matrix[V][i] ==1 and visited[i] == 0:
            dfs(i)


dfs(V)
print()
bfs(V)

