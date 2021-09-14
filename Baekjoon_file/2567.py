import sys
sys.setrecursionlimit(1000000000)

n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

x_list = []
y_list = []
for i in range(n):
    a,b = map(int,input().split())
    x_list.append(a)
    y_list.append(b)

matrix = [[0 for _ in range(101)] for _ in range(101)]



while x_list:
    a = x_list.pop()
    b = y_list.pop()
    for i in range(a,a+10):
        for j in range(b,b+10):
            matrix[i][j] = 1

sum = 0
for i in range(1,101):
    for j in range(1,101):
        if matrix[i][j] == 1:
            for k in range(4):
                x1 = dx[k] + i
                y1 = dy[k] + j
                if 0 <= x1 < 101 and 0<= y1 < 101:
                    if matrix[x1][y1] == 0:
                        sum+=1

print(sum)
