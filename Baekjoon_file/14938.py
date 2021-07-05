#정점 개수,수색범위,간선 개수
n,m,r = map(int,input().split())
INF = int(1e9)
#각 지역마다 갖고있는 value
value_list = [0]
value_list = value_list + list(map(int,input().split()))

matrix = [[INF]*(n+1) for _ in range(n+1)]
answer_node = [0 for _ in range(n+1)]
for i in range(r):
    #인접 행렬(간선 표시)
    a,b,c = map(int,input().split())
    matrix[a][b] = c
    matrix[b][a] = c

for i in range(n+1):
    matrix[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for i in range(n+1):
    for j in range(n+1):
        if matrix[i][j] <= m:
            answer_node[i] += value_list[j]

print(max(answer_node))
