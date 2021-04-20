t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    #큐로 해당 좌표 받음
    queue = [(x, y)]
    #큐가 빌때까지 무한 루프
    while queue:
        #큐에서 좌표 뽑기
        a, b = queue.pop()
        for i in range(4):
            #동서남북으로 좌표 탐색
            q = a + dx[i]
            w = b + dy[i]
            #좌표가 이상 없고 탐색했을때 좌표가 1일때
            if 0 <= q < n and 0 <= w < m and s[q][w] == 1:
                #탐색 즉 근처에 있는 좌표 0으로 만듬.
                s[q][w] = 0
                queue.append((q, w))
for i in range(t):
    m, n, k = map(int, input().split())
    # 초기 값 0으로 기본 배열 생성
    s = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        #주어진 좌표에 1표시
        a, b = map(int, input().split())
        s[b][a] = 1
    for q in range(n):
        for w in range(m):
            #이중포문으로 해당좌표에 1이있으면 bfs 실시
            if s[q][w] == 1:
                bfs(q, w)
                #그해당좌표 0으로 만듬.
                s[q][w] = 0
                cnt += 1
    print(cnt)