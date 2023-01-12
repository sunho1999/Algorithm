
n = int(input())
dp = [[0 for _ in range(9)]for _ in range(1000)]

        #1,2,3,4,5,6,7,8,9
dp[0] = [1,1,1,1,1,1,1,1,1] # 초기 세팅
dp[1] = [9,8,7,6,5,4,3,2,1]
if n == 1:
    print(sum(dp[n-1])+1)
elif n == 2:
    print(sum(dp[n-1]) + sum(dp[n-2])+1)
else:
    for i in range(3,n+1):
        for j in range(9):
            dp[i-1][j] = sum(dp[i-2][j:10]) % 10007
    answer = 0
    for i in range(n):
        answer += sum(dp[i])
    print((answer+1)% 10007)
# 0,1,2,3,4,5,6,7,8,9 10개
#
# 1(1~9) 9
# 2(2~9) 8
# 3(3~9) 7
# 4(4~9) 6
# 5(5~9) 5
# . 4
# . 3
# . 2
#  1
#

# 1xx -> 45개       (3자리수)
# 2xx -> 36개
# 3xx -> 28개
# 4xx -> 21개
# 5xx -> 15개
# 6xx -> 10개
# 7xx -> 6개
# 8xx -> 3개
# 9xx -> 1개

# 1xxx -> (45+36+28+21+15+10+6+3+1)