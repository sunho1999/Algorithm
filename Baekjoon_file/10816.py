import sys

#총 카드수
num = sys.stdin.readline()
card_list = list(map(int,sys.stdin.readline().split()))
#보유 카드수
a = sys.stdin.readline()
#확인해야할 카드
check_card = list(map(int,sys.stdin.readline().split()))
#확인한 답 넣을 리스트
answer = []

for i in check_card:
    if i in card_list:
        answer.append(card_list.count(i))
    elif i not in card_list:
        answer.append(0)
for i in answer:
    print(i,end= " ")

