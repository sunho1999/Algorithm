import sys
input=sys.stdin.readline

number= [0]+list(input().strip())
if number[1]=='0':
    print(0)
    exit()

dp=[1,1]+[0] * (len(number)-2)

for i in range(2, len(number)):
    num1=int(number[i])
    num2=int(number[i-1])*10+int(number[i])
    if num1>0: dp[i]+=dp[i-1]
    if num2>=10 and num2<=26: dp[i]+=dp[i-2]

print(dp[len(number)-1]%1000000)