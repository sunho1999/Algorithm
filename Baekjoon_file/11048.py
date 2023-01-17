N,M = map(int,input().split())

matrix = []
for i in range(N): # 초기값 세팅
    list1 = list(map(int,input().split()))
    matrix.append(list1)

dx = [1,0,1]
dy = [0,1,1]
dp = [[0 for _ in range(M+1)] for _ in range(N+1)] # dp 초기 배열 설정
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = matrix[i-1][j-1] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) # 점화식

print(dp[N][M])