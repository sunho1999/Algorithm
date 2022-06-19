import string
n = int(input())
strin = input()

def hash_function(strin):
    alpha = ["@"]
    alpha = alpha + list(string.ascii_lowercase)
    print(alpha)
    M = 1234567891
    r = 31
    answer = 0
    for i in range(len(strin)):
        if strin[i] in alpha:
            a = alpha.index(str(strin[i]))
            answer += a * (r ** i)
    return answer%M

print(hash_function(strin))


