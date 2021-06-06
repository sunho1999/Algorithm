from itertools import combinations

n,m= map(int, input().split())
matrix = []
for i in range(n):
  matrix.append(list(map(int, input().split())))

home=[]
chicken=[]
for i in range(n):
  for j in range(n):
    if matrix[i][j]==1:
      home.append((i,j))
    elif matrix[i][j]==2:
      chicken.append((i,j))


pick_chicken=list(combinations(chicken,m))
result=[0]*len(pick_chicken)

for i in home:
  for j in range(len(pick_chicken)):
    a=10000
    for k in pick_chicken[j]:
      temp = abs(i[0]-k[0])+abs(i[1]-k[1])
      a = min(a,temp)
    result[j]+=a

print(min(result))