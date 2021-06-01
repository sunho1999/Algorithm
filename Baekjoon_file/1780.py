import sys
n = int(input())

matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result_1 = 0
result0 = 0
result1 = 0



def cut(x,y,n):
    global result1,result0,result_1
    check = matrix[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != matrix[i][j]:
                for k in range(3):
                    for z in range(3):
                        cut(x+n//3*k,y+n//3*z,n//3)
                return

    if check == -1:
        result_1+=1
    elif check == 0:
        result0 +=1
    elif check == 1:
        result1 +=1

cut(0,0,n)
print(result_1)
print(result0)
print(result1)









