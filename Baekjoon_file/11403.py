from collections import deque

n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]

def dfs(i):
    for j in range(n):
        for k in range(n):
            if matrix[j][k] == 1 or (matrix[j][i] ==1 and matrix[i][k] == 1):
                matrix[j][k] = 1
for i in range(n):
    dfs(i)


for i in matrix:
    for j in i:
        print(j,end = " ")
    print()