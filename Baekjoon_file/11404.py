import sys
inf = 10000000
n = int(input())
m = int(input())

cost = [[inf]*n for i in range(n)]

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    cost[a-1][b-1] = min(cost[a-1][b-1],c)

#경유지
for i in range(n):
    cost[i][i] = 0
    #출발지
    for j in range(n):
        #도착지
        for k in range(n):
            cost[j][k] = min(cost[j][k], cost[j][i]+cost[i][k])

for i in cost:
    for j in range(n):
        if i[j] == inf:
            i[j] = 0
        print(i[j], end= " ")
    print()