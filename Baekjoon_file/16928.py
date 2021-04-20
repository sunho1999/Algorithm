
from collections import deque

#사다리 수, 뱀 수
N,M = map(int,input().split())
#사다리 값 저장
ladder = [0 for i in range(101)]
# 스네이크 저장
snake = [0 for _ in range(101)]
#방문한 수 저장
visited = [0 for j in range(101)]

que = deque()
for i in range(N):
    a,b = map(int,input().split())
    ladder[a] = b

for i in range(M):
    a,b = map(int,input().split())
    snake[a] = b
#초기값 설정
que.append((1,0))
visited[1] = True
val = 0
while que:
    idx = que.popleft()
    #좌표
    loc = idx[0]
    #굴린 수
    cnt = idx[1]
    if loc == 100:
        val = cnt
        continue
    #주사위 굴리기
    for i in range(1,7):
        new = loc + i
        #100넘어가면 그냥 넘어가기
        if new > 100:
            continue
        #방문햇던 장소면 그냥 넘어가기
        if visited[new] == 1:
            continue
        #방문 안한 장소 체크
        visited[new] = 1
        #스네이크 도달시 그 인덱스 값 추출
        if snake[new] != 0:
            new = snake[new]
        #사다리 도달시 그 인덱스 값 추출
        if ladder[new] != 0:
            new = ladder[new]
        #도달하면서 얻은 값 다시 큐에 저장
        que.append((new,cnt+1))
print(val)
