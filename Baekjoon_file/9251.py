a1 = input()
a2 = input()

matrix = [[0]*(len(a2)+1) for i in range(len(a1)+1)]

for i in range(1,len(a1)+1):
    for j in range(1,len(a2)+1):
        if a1[i-1] == a2[j-1]:
            matrix[i][j] = matrix[i-1][j-1]+1
        else:
            matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])

print(matrix[-1][-1])