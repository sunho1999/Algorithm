import sys

n,k = map(int,sys.stdin.readline().split())

dp = [[0]*(n+1) for _ in range(k+1)]


if k == 1:
    print(1)
elif k == 2:
    print(n+1)
else:
    for i in range(1,n+1):
        dp[1][i] = 1
    for i in range(1,n+1):
        dp[2][i] = i+1

    for i in range(2,k+1):
        dp[i][1] = i
        for j in range(2,n+1):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j])%1000000000

    print(dp[k][n])
