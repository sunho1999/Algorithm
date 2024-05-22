import sys
input = sys.stdin.readline

n = int(input())
matrix = []

for i in range(n):
    a = list(map(int,input().strip()))
    matrix.append(a)


def division(start,end,gap):
    start_number = matrix[start][end]
    check = True
    for i in range(start,start+gap):
        for j in range(end,end+gap):
            if start_number != matrix[i][j] and check:
                check = -1
                break
    if check == -1:
        print("(",end="")
        gap =gap//2
        division(start,end,gap) # 0,4,4
        division(start,end + gap,gap) #4,8,4
        division(start + gap ,end, gap) # 4,0,4
        division(start+gap, end+gap,gap)
        print(")",end="")
    elif check == True and start_number == 1:
        print(1,end="")
    elif check == True and start_number == 0:
        print(0,end="")

division(0,0,n)
