N,M = map(int,input().split())
tree = list(map(int,input().split()))

# 원하는 나무의 양을 target에 대입.
# start, mid , end := 톱의 높이
def treeSum(height):
    Sum = 0
    for i in tree:
        if i-height >0:
            Sum+=(i-height)

    return Sum

def binarySearch(target):
    start,end=0, max(tree)
    ans = 0
    while(start<=end):
        mid = (start+end)//2
        Sum = treeSum(mid)
        if Sum < target :
            end = mid -1
        if Sum >= target:
            ans = mid
            start = mid + 1

    return ans

print(binarySearch(M))