
def checking(temp,sticker):
    for cy in range(len(sticker)):
        for cx in range(len(sticker[0])):
            if temp[i+cy][j+cx] + sticker[cy][cx] > 1:
                return False
    return True

def attach(temp,sticker):
    for cy in range(len(sticker)):
        for cx in range(len(sticker[0])):
            temp[i + cy][j + cx] += sticker[cy][cx]
    return

def rotate_90(arr):
    c = len(arr)
    d = len(arr[0])

    result = [[0]*c for _ in range(d)]

    for i in range(c):
        for j in range(d):
            result[j][c-i-1] = arr[i][j]
    return result

n,m,k = map(int,input().split()) #  세로, 가로, 스티커 개수
board = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    r,c = map(int,input().split()) # 행, 열
    sticker = [list(map(int,input().split())) for _ in range(r)]

    check = False # 붙일 수 있는지 없는지 판별하는 변수
    cnt = 0 # rotate 횟수

    while cnt < 4:
        if check == True:
            break
        for i in range(n-len(sticker)+1): # 세로길이 만큼 뛰기
            if check == True:
                break
            for j in range(m-len(sticker[0])+1): # 가로 길이 만큼 뛰기
                if checking(board,sticker): # 보드에 스티커 붙일 수 있는지 판별
                    attach(board,sticker)
                    check = True
                    break
        sticker = rotate_90(sticker)
        cnt += 1

answer = 0

for i in range(n):
    for j in range(m):
        answer += board[i][j]

print(answer)

