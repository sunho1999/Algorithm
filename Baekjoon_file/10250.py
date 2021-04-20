test_case = int(input())
answer = 0
for i in range(test_case):
    list1 = list(map(int,input().split()))
    hosu = list1[2]//list1[0]+1
    floor = list1[2]%list1[0]
    if floor ==0:
        floor = list1[0]
        hosu = hosu -1
    print(floor*100+hosu)