n,m = map(int,input().split())

matrix = []
cnt = 0
for i in range(n):
    a = input()
    matrix.append(list(map(int,list(a))))

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i-1][j-1] == 1:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) +1
            if dp[i][j] > cnt:
                cnt = dp[i][j]

print(cnt**2)