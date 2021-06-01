import sys,collections,copy

n,m = map(int,sys.stdin.readline().split())
max_num = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]
empty_list = []
virus_list = []

Empty = 0
Wall = 1
Virus = 2

g = [[0]*m for _ in range(n)]

#입력 받으면서 바로 바이러스랑 빈 공간 좌표값 저장
for y in range(n):
    raw = [int(a) for a in sys.stdin.readline().split()]
    for x in range(m):
        g[y][x] = raw[x]
        if g[y][x] == Empty:
            empty_list.append([y, x])
        if g[y][x] == Virus:
            virus_list.append([y, x])

def bfs(ng):
    q = collections.deque([])
    #방문리스트 생성
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    global max_num
    #바이러스 좌표값 큐에 추가
    for virus in virus_list:
        q.append(virus)
    while q:
        cy, cx = q.popleft()
        #4방향 탐색
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            #빈공간이면서 방문하지 않은 좌표일떄 큐에 추가 후 바이러스로 바꾸기
            if ng[ny][nx] == Empty and visited[ny][nx] == False:
                q.append([ny, nx])
                ng[ny][nx] = Virus
                visited[ny][nx] = True
    #바이러스가 다 탐색한후 empty공간 찾기
    for i in range(n):
        cnt += ng[i].count(Empty)
    #매번 탐색이 끝난후 empty공간이 많으면 바꾸기
    if max_num < cnt:
            max_num = cnt

for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            #n부터 1까지 n-1부터 1까지 n-2부터 1까지 empty좌표 다 탐색해서 임의로 벽 생성
            y1, x1 = empty_list[i]
            y2, x2 = empty_list[j]
            y3, x3 = empty_list[k]

            g[y1][x1] = Wall
            g[y2][x2] = Wall
            g[y3][x3] = Wall
            ng = copy.deepcopy(g)
            bfs(ng)
            #다시 벽 초기화
            g[y1][x1] = Empty
            g[y2][x2] = Empty
            g[y3][x3] = Empty


print(max_num)


