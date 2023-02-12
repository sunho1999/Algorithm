import  sys
input = sys.stdin.readline
n = int(input())

date_list = []
for i in range(n):
    start_m, start_d, end_m, end_d = map(int,input().split())
    date_list.append((start_m*100+start_d,end_m*100+end_d))

date_list.sort() # 시작날짜가 적은 순대로 정렬하여 탐색 진행
cnt = 0
end_date = 301 # 끝나는 날짜를 저장할 변수
while(date_list):
    if end_date >= 1201 or date_list[0][0] > end_date:
        break
    temp_date = -1# 현재 진행하는 날자를 저장할 변수
    for _ in range(len(date_list)):
        if end_date >= date_list[0][0]: # end_date가 시작날짜보다 크면
            if temp_date <= date_list[0][1]:
                temp_date = date_list[0][1]

            date_list.remove(date_list[0])
        else:
            break
    end_date = temp_date
    cnt +=1

if end_date < 1201:
    print(0)
else:
    print(cnt)

