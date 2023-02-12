import  sys
input = sys.stdin.readline
n,k = map(int,input().split())

student_list = list(map(int,input().split()))

gap_list = []
gap = 0
for i in range(len(student_list)-1):
    gap = abs(student_list[i]-student_list[i+1])
    gap_list.append(gap)
index_list = []
gap_list.sort()
# print(gap_list)

# print(gap_list[:-(k-1)])
print(sum(gap_list[:n-k]))
