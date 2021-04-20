from collections import deque

N, M = map(int,input().split())
#초기 배열 생성
matrix = [[N for k in range(N+1)] for i in range(N+1)]
#큐 생성
que = deque()
#값 담을 리스트
res = []


#좌표값 쌍방향으로 저장
for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1


#플로이드 와샬 알고리즘 적용
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
matrix.remove(matrix[0])

#값 다더하기
for i in matrix:
    res.append(sum(i))

print(res.index(min(res))+1)