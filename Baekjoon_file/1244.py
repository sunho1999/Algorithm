switch_num = int(input())

dummy = ['@']
switch = list(map(int,input().split()))

switch = dummy + switch

testcase = int(input())
cnt = 1
check_L = 0
check_R = 0

for i in range(testcase):
    a,b = map(int,input().split())

    if a == 1:
        for j in range(1*b,switch_num+1,b):
            if switch[j] == 1:
                switch[j] = 0
            else:
                switch[j] = 1
        print(switch)
    elif a == 2:
        if 1<= b-cnt and b+cnt < switch_num:
            check_L = switch[b-cnt]
            check_R = switch[b+cnt]

            while (check_L == check_R):
                check_L = switch[b - cnt]
                check_R = switch[b + cnt]
                if 1 <= b - cnt and b + cnt < switch_num:
                    if check_L == check_R: # 좌우 같다면
                        if switch[b-cnt] == 1:
                            switch[b-cnt] = 0
                            switch[b+cnt] = 0
                        else:
                            switch[b - cnt] = 1
                            switch[b + cnt] = 1
                cnt +=1
            check_L = switch[b - cnt]
            check_R = switch[b + cnt]
            if check_L != check_R:
                if switch[b] == 1:
                    switch[b] = 0
                elif switch[b] == 0:
                    switch[b] = 1



for i in range(1,len(switch)):

    print(switch[i],end = " ")
    if i % 20 == 0:
        print()
