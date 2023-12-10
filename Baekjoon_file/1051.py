n,m = map(int,input().split())
matrix = []
for i in range(n):
    a = list(input())
    matrix.append(a)
# print(matrix)

min_num = min(n,m)  # ex)3 최대 정사각형 크기는 3이 넘을 수 없음
# range_len = min_num +1
answer = []


while True:
    for i in range(n-min_num):
        for j in range(m-min_num):
         # print(i,j)
            if matrix[i][j] == matrix[i][j+min_num] == matrix[i+min_num][j] == matrix[i+min_num][j+min_num]:
                # print(matrix[i][j])
                # print(min_num)
                print((min_num+1)**2)
                exit()
    else:
        min_num-=1