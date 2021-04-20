
def div(a,b):

    if b == 1:
        return a % C
    else:
        left = div(a, b // 2)
        # a**10 = (a**5)**2
        if b % 2 == 0:
            return (left*left)%C
        # a**11 = (a**5)**2 * a
        elif b % 2 == 1:
            return (left*left)*a%C



if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(div(A,B))

