t = int(input())

for i in range(t):
    s = []
    n = int(input())
    for j in range(2):
        s.append(list(map(int,input().split())))
    #기본 첫번째 인덱스 값 고정
    s[0][1] = s[0][1]+s[1][0]
    s[1][1] = s[1][1]+s[0][0]
    for k in range(2,n):
        s[0][k] = max(s[1][k-1],s[1][k-2]) + s[0][k]
        s[1][k] = max(s[0][k-1],s[0][k-2]) + s[1][k]

    print(max(s[0][n-1],s[1][n-1]))
