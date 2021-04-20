import sys

num = int(sys.stdin.readline())

color_list =[]

for i in range(num):
    a = list(map(int,sys.stdin.readline().split()))
    color_list.append(a)
#dp
#전 색의 합을 구한다음 그중 최소값과 현재 고른 색의 값을 더해서 현재 색에 추가, 이를 반복해서 계속 합을 쌓아감
for i in range(1,num):
    #빨간색
    color_list[i][0] = min(color_list[i-1][1],color_list[i-1][2])+color_list[i][0]
    #초록색
    color_list[i][1] = min(color_list[i-1][0],color_list[i-1][2])+color_list[i][1]
    #파란색
    color_list[i][2] = min(color_list[i-1][0],color_list[i-1][1])+color_list[i][2]

print(min(color_list[num-1]))