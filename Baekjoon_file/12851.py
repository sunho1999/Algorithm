import sys
from collections import deque
a, b = map(int,sys.stdin.readline().split())
visited = [0]*100001
#방문기록 숫자 증가
cnt = 0
#bfs하기위한 큐 생성
q = deque([[a,cnt]])

print(q)
while q:
    node = q.popleft()
    cnt = node[0]
    way = node[1]
    bbb = 0
    if cnt == b:
        bbb+=1
        print(way)
        print(bbb)
        break
    else:
        if visited[cnt-1] == 0 and 0 <= cnt <= 100001:
            visited[cnt-1] = visited[cnt] +1
            q.append([cnt-1,way+1])

        if visited[cnt+1] == 0 and 0 <= cnt <= 100001:
            visited[cnt+1] = visited[cnt] +1
            q.append([cnt+1,way+1])
        if visited[cnt*2] == 0 and 0 <= cnt <= 100001:
            visited[cnt*2] = visited[cnt] +1
            q.append([cnt*2,way+1])
