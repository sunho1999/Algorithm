n = int(input())

board = [list(input()) for _ in range(n)]
# print(board)

def row():
    max_cnt = 0
    for i in range(n):
        cnt = 1
        for j in range(n):
            if j >=0 and j < n-1:
                if board[i][j] == board[i][j+1]:
                    cnt +=1
                    if max_cnt < cnt:
                        max_cnt = cnt
                else:
                    cnt =1
    return max_cnt

def column():
    max_cnt = 0
    for i in range(n):
        cnt = 1
        for j in range(n):
            if j >=0 and j < n-1:
                if board[j][i] == board[j+1][i]:
                    cnt +=1
                    if max_cnt < cnt:
                        max_cnt = cnt
                else:
                    cnt =1
    return max_cnt

total_cnt = 0
for i in range(n): # 0, 1, 2
    for j in range(n-1): # 0, 1, 2
        if board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # swap
            row_cnt = row()
            column_cnt = column()
            if row_cnt >= column_cnt:
                if total_cnt < row_cnt:
                    total_cnt = row_cnt
            else:
                if total_cnt < column_cnt:
                    total_cnt = column_cnt
            board[i][j+1],board[i][j] = board[i][j],board[i][j+1]

        if board[j][i] != board[j+1][i]:
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i] # swap
            row_cnt = row()
            column_cnt = column()
            if row_cnt >= column_cnt:
                if total_cnt < row_cnt:
                    total_cnt = row_cnt
            else:
                if total_cnt < column_cnt:
                    total_cnt = column_cnt
            board[j+1][i],board[j][i] = board[j][i],board[j+1][i]
print(total_cnt)

