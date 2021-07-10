from collections import deque

n,k = map(int,input().split())

cnt = 0
que = deque()
#초기 설정
time_list = [-1 for _ in range(1000001)]
visited = [0 for _ in range(1000001)]

visited[n] = 1
time_list[n] = 0

que.append(n)
while que:
    a = que.popleft()
    if a*2 <= 100001 and visited[a*2] == 0:
        visited[a*2] = 1
        time_list[a*2] = time_list[a]
        que.appendleft(a*2)
    if a-1 >= 0 and visited[a-1] == 0:
        visited[a-1] = 1
        time_list[a-1] = time_list[a] +1
        que.append(a-1)
    if a+1 <= 100001 and visited[a+1] == 0:
        visited[a+1] = 1
        time_list[a+1] = time_list[a] +1
        que.append(a+1)


print(time_list[k])



