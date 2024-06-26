n = int(input())
M = list(map(int, input().split()))
W = list(map(int, input().split()))
M.sort()
W.sort()
answer = 0
start = 0
end = n-1
while start<n and 0<=end:
    if M[start]<0 and 0<W[end] and abs(M[start])>W[end]:
        answer += 1
        start += 1; end -= 1
    elif M[start]<0 and 0<W[end] and abs(M[start])<=W[end]:
        end -= 1
    elif 0<M[start] and W[end]<0 and M[start] < abs(W[end]):
        answer += 1
        start +=1; end -= 1
    elif 0<M[start] and W[end]<0 and M[start] >= abs(W[end]):
        end -= 1
    elif M[start]<0 and W[end]<0:
        start += 1
    elif 0<M[start] and 0<W[end]:
        end -= 1

print(answer)