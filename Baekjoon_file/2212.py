# 고속도로 위에 최대 K개의 집중국을 세울 수 있음.
# N개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 하며, 집중국의 유지비 문제로 인해 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야 함.
# 각 집중국의 수신 가능영역의 거리의 합의 최솟값을 구하는 프로그램을 작성하시오. 단, 집중국의 수신 가능영역의 길이는 0 이상이며 모든 센서의 좌표가 다를 필요는 없다.

n = int(input()) # 센서의 개수
k = int(input()) # 집중국의 개수
sensor_n = list(map(int,input().split())) # N개의 센서의 좌표
sensor_n.sort()

number_list = []
for i in range(len(sensor_n)-1):
    number_list.append(sensor_n[i+1] - sensor_n[i])

number_list.sort()
if k == 1:
    print(sum(number_list))
else:
    print(sum(number_list[:-(k-1)]))