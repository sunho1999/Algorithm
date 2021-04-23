n = int(input())

tri = []
sum = 0
for i in range(n):
    tri.append(list(map(int,input().split())))

a = 2
for i in range(1,n):
    for j in range(a):
        if j == i:
            tri[i][j] = tri[i][j] + tri[i-1][j-1]
        elif j == 0:
            tri[i][j] = tri[i-1][j] + tri[i][j]
        else:
            tri[i][j] = max(tri[i][j]+ tri[i-1][j-1], tri[i][j]+tri[i-1][j])
    a+=1

print(max(tri[n-1]))