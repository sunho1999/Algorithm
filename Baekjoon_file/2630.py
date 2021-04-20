import sys

def quad_tree(x,y,n):
    global matrix,blue,white
    color = matrix[y][x]
    breakpoint = False

    for i in range(x,x+n):
        if breakpoint:
            break
        for j in range(y,y+n):
            if matrix[j][i] != color:
                quad_tree(x,y,n//2) #2사분면
                quad_tree(x,y+n//2,n//2)#3사분면
                quad_tree(x+n//2,y,n//2)#1사분면
                quad_tree(x+n//2,y+n//2,n//2)
                breakpoint = True
                break
    if not breakpoint:
        if matrix[y][x] == 1:
            blue +=1
        else:
            white +=1





N = int(input())
matrix = []
blue = 0
white = 0

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

quad_tree(0,0,N)
print(white)
print(blue)