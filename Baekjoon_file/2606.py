from collections import deque
#노드 갯수
node_num = int(input())
#간선 갯수
line_num = int(input())
visited = [0]*(node_num+1)
visited[1] = 1
matrix = [[0]* (node_num+1) for i in range(node_num+1)]
q = deque()
q.append(1)
for i in range(line_num):
    a,b = map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1
while q:
    a = q.popleft()
    for i in range(node_num+1):
        if matrix[a][i] == 1 and visited[i] == 0:
            visited[i] = 1
            q.append(i)
print(visited.count(1)-1)





