testcase = int(input())

for i in range(testcase):
    text = input()
    left_idx = 0
    right_idx = len(text)-1
    chance = True
    check = True
    while(left_idx <= right_idx):
        if check == False:
            break
        # print(left_idx,right_idx)
        if text[left_idx] == text[right_idx]: # 왼쪽 오른쪽 같을 경우
            left_idx +=1
            right_idx -=1
        else: # 왼쪽 오른쪽 다를 경우
            if left_idx < right_idx - 1:  # 인덱스 확인하기
                temp = text[:right_idx] + text[right_idx + 1:]
                if temp[:] == temp[::-1]:
                    chance = False
                    break
                # 왼쪽 문자열 제거
            if left_idx + 1 < right_idx:
                temp = text[:left_idx] + text[left_idx + 1:]
                if temp[:] == temp[::-1]:
                    chance = False
                    break
            check = False
            break
    if check == False:
        print(2)
    elif check == True and chance == False:
        print(1)
    elif check== True and chance == True:
        print(0)
