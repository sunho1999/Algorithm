#전체 테스트케이스 수
testcase = int(input())
for i in range(testcase):
    coin_case = int(input())
    coin_list = map(int,input().split())
    coin_goal = int(input())
    dp = [0 for _ in range(coin_goal+1)]
    dp[0] = 1

    for k in coin_list:
        for z in range(1,coin_goal+1):
            if z - k >= 0:
                dp[z] = dp[z] + dp[z-k]

    print(dp[coin_goal])
