num = int(input())
#점화식 리스트 만들기
list = [0 for i in range(10000000)]
#초항 두번째항 고정
list[0] = 1
list[1] = 6
idx_count = 2
sum = 7
if num == 1:
    print(1)
elif num >=2 and num <= 7:
    print(2)
else:
    #점화식 구현
    while(True):
        list[idx_count] = (list[idx_count-1])+6
        sum = list[idx_count] + sum
        idx_count +=1
        if sum >= num and num > list[idx_count]:
            print(idx_count)
            break

