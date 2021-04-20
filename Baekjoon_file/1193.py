n = int(input())
sum =0
count =0
#sum 순서 확인
while(count<n):
    sum +=1
    count+=sum
#구한 count로 분모 또는 분자 만들기
count -= sum
#짝수일때 홀수일때 구하기
if sum %2 ==0:
    i = n-count
    j = sum-i+1
else:
    i = sum - (n-count) + 1
    j = n-count

print(f"{i}/{j}")


