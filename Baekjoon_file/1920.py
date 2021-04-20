N = int(input())
#비교할 리스트
list_a = list(map(int,input().split()))
list_a.sort()
M = int(input())
#원소 하나씩 비교할 리스트
list_b = list(map(int,input().split()))


def binary(i,list_a,left,right):
    if left > right:
        return 0
    mid = (left+right)//2
    if i == list_a[mid]:
        return 1
    elif i < list_a[mid]:
        return binary(i,list_a,left,mid-1)
    else:
        return binary(i,list_a,mid+1,right)


for i in list_b:
    left = 0
    right = len(list_a)-1
    print(binary(i,list_a,left,right))