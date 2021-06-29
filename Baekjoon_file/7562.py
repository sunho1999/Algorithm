from  collections import  deque
testcase = int(input())

dx = [-2,-1,-2,-1,1,2,1,2]
dy = [-1,-2,1,2,-2,-1,2,1]

def bfs(a,b):
    visited = [[0]*num for _ in range(num)]
    que = deque()
    que.append([a,b])
    visited[a][b] = 1
    while que:
        x,y = que.popleft()
        if x == end_x and y == end_y:
            print(visited[end_x][end_y] - 1)
            return
        for i in range(8):
            x1 = dx[i] + x
            y1 = dy[i] + y
            if 0 <= x1 < num and 0 <= y1 < num:
                if visited[x1][y1] == 0:
                    visited[x1][y1] = visited[x][y] +1
                    que.append([x1,y1])


for i in range(testcase):
    # a*a matrix
    num = int(input())
    #x,y 시작좌표
    x,y = map(int,input().split())
    #end_x,end_y 도착좌표
    end_x, end_y = map(int,input().split())
    bfs(x,y)




