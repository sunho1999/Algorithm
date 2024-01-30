
def dfs(v,i):
    visited[v]=True
    w=data[v]
    if not visited[w]:
        dfs(w,i)
    elif visited[w] and w==i:
        result.append(w)
n = int(input())
data = [0]+[int(input()) for _ in range(n)]
result = []
for i in range(1,n+1):
    visited = [0]*(n+1)
    dfs(i,i)
print(len(result))
result.sort()
for i in result:
    print(i)