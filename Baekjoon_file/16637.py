# 괄호 안에는 연산자가 하나만 들어 있어야 한다.

n = int(input())
result = -9999999999

text = list(input())
# print(text)



def calculate(now,operation,next):
    if operation == "-":
        num = now - next
    elif operation == "+":
        num = now + next
    elif operation == "*":
        num = now * next
    return  num

def dfs(idx, value):
    global result
    if idx == n-1:
        result = max(result,value)
        return
    else:
        if idx + 2 < n:
            next_value = calculate(value,text[idx+1],int(text[idx+2]))
            dfs(idx+2,next_value)

        if idx + 4 < n:
            next_next_value = calculate(int(text[idx+2]),text[idx+3],int(text[idx+4]))
            next_value = calculate(value,text[idx+1],next_next_value)
            dfs(idx+4,next_value)




dfs(0,int(text[0]))
print(result)