melon = int(input())

list1= [] # 방향 정보 담을 리스트
width = [] # min, max 구할 리스트
length = []
for i in range(6):
    dirc,line = map(int,input().split())
    list1.append((dirc,line))
    if dirc == 2 or dirc == 1:
        width.append(line)
    elif dirc == 3 or dirc == 4:
        length.append(line)
# print(list1)
min_field = []
for i in range(6):
    if list1[i][0] == list1[(i+2)%6][0]:
        min_field.append(list1[(i+1)%6][1])

max_filed = max(width) * max(length)
min_field = min_field[0] * min_field[1]
print((max_filed-min_field) * melon)