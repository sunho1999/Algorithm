from collections import deque

r,c = map(int,input().split())

matrix = [list(input().strip()) for i in range(r)]

#방문노드
visit = [[0] * c for _ in range(r)]
#좌,우,상,하
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#고슴도치,물 시작 좌표 담음
point_go = deque()
point_water = deque()

for i in range(r):
    for j in range(c):
        #물좌표 저장
        if matrix[i][j] == "*":
            point_water.append([i,j])
        #고슴도치 좌표 저장
        elif matrix[i][j] == "S":
            point_go.append([i,j])
            visit[i][j] = 1
            matrix[i][j] = 0
        #비버 좌표 저장
        elif matrix[i][j] == "D":
            point = [i,j]


def bfs():
    while point_go or point_water:
        temp1 = []
        temp2 = []
        #고슴도치
        while point_go:
            x1,y1 = point_go.popleft()
            if matrix[x1][y1] != "*":
                for i in range(4):
                    #고슴도치
                    a1 = dx[i] + x1
                    b1 = dy[i] + y1

                    if 0 <= a1 < r and 0<= b1 < c :
                        if visit[a1][b1] == 0 and matrix[a1][b1] != "X" and matrix[a1][b1] != '*':
                            matrix[a1][b1] = matrix[x1][y1] +1
                            visit[a1][b1] = 1
                            temp1.append([a1,b1])
        #물
        while point_water:
            x2,y2 = point_water.popleft()
            for i in range(4):
                a2 = dx[i] + x2
                b2 = dy[i] + y2
                #비버집이면 그냥 패스
                if a2 == point[0] and b2 ==point[1]:
                    continue
                if 0 <= a2 < r and 0 <= b2 < c:
                    if matrix[a2][b2] != "*" and matrix[a2][b2] != "X":
                        matrix[a2][b2] = "*"
                        temp2.append([a2,b2])
        for i in temp1:
            point_go.append(i)
        for i in temp2:
            point_water.append(i)




bfs()
result = matrix[point[0]][point[1]]
print(result if result != "D" else "KAKTUS")