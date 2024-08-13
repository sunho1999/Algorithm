import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def move(check_num):
    y,x,z = chess[check_num]
    if check_num != chess_map[y][x][0]:
        return
    xx = dx[z] + x
    yy = dy[z] + y
    if not 0 <= xx < n or not 0 <= yy < n or a[yy][xx] == 2: # 벽에 부딪히거나, 파란색 좌표를 만났을 때
        if 0 <= z <= 1:  # 왼쪽, 오른쪽이면 방향 바꿈
            nz = (z + 1) % 2
        else: # 위쪽,아래쪽이면 방향 바꿈
            nz = (z - 1) % 2 + 2
        chess[check_num][2] = nz # 방향 바꾼걸로 바꿈
        xx = x + dx[nz]
        yy = y + dy[nz]
        if not 0 <= xx < n or not 0 <= yy < n or a[yy][xx] == 2: # 갇혔을 때 return
            return 0
    chess_set = []
    chess_set.extend(chess_map[y][x])
    chess_map[y][x] = []

    if a[yy][xx] == 1:  #
        chess_set = chess_set[-1::-1]

    for i in chess_set:
        chess_map[yy][xx].append(i)
        chess[i][:2] = [yy, xx]

    if len(chess_map[yy][xx]) >= 4:
        return 1
    return 0

n,k = map(int,input().split())

# 0은 흰색, 1은 빨간색, 2는 파란색
point_list = []
a = [list(map(int,input().split() ))for i in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
chess = [0 for _ in range(k)] # 좌표, 방향 넣을 변수

# dir 1: 오른쪽, 2: 왼쪽, 3: 위쪽, 4: 아래쪽
for i in range(k):
    y,x,dir = map(int,input().split())
    chess_map[y-1][x-1].append(i)
    chess[i] = [y-1,x-1,dir-1]
# print(chess)
# print(chess_map)

cnt = 1
while cnt <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()
    cnt += 1
print(-1)