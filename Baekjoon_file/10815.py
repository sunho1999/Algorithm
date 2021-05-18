import sys
n = int(input())
#상근이가 가지고 있는 카드
basic_card = list(map(int,sys.stdin.readline().split()))
basic_card.sort()
#상근이가 체크할 카드
m = int(input())
check_card = list(map(int,sys.stdin.readline().split()))


def binary(num):
    l = 0
    r = n-1
    while l <= r:
        mid = (l+r)//2
        if num == basic_card[mid]:
            return 1
        elif basic_card[mid] > num:
            r = mid -1
        else:
            l = mid +1
    return 0

for i in check_card:
    print(binary(i), end =" ")