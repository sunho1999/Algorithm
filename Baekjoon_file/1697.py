from collections import deque

start_point, end_point = map(int,input().split())

visited = [0 for i in range(100002)]

que = deque()
que.append(start_point)

while que:
    x = que.popleft()

    if x == end_point:
        print(visited[x])
        break
    if x-1 >=0 and x-1 <= 100001 and visited[x-1] == 0:
        visited[x-1] = visited[x]+1
        que.append(x-1)
    if x +1 >= 0 and x+1 <= 100001 and visited[x+1] == 0:
        visited[x+1] = visited[x]+1
        que.append(x+1)
    if x*2 >=0 and x*2 <= 100001 and visited[x*2] == 0:
        visited[x*2] = visited[x]+1
        que.append(x*2)

# 100 98일때 안됨.