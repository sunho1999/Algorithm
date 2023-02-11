
n = int(input())

dp = [0 for _ in range(1001)]
dp[0] = 1
dp[1] = 2
if n == 1:
    print(dp[n - 1])
    exit()
elif n == 2:
    print(dp[n - 1])
    exit()
for i in range(2,n+1):
    if i >= 3:
        dp[i-1] = (dp[i-2] + dp[i-3])%10007
print(dp[n-1])