x,y,w,h = map(int, input().split())

ave_x = w/2
ave_y = h/2
#3사분면
if ave_x > x and ave_y > y:
    if ave_x-x > ave_y-y:
        print(x)
    elif ave_x-x < ave_y-y:
        print(y)
#4사분면
elif ave_x < x and ave_y > y:
    if x-ave_x > ave_y-y:
        print(y)
    elif ave_x-x> x-ave_x:
        print(w-x)
#2사분면
elif ave_x >x and ave_y < y:
    if ave_x - x > y-ave_y:
        print(h-y)
    elif ave_x -x < y-ave_y:
        print(x)
#1사분면
elif ave_x < x and ave_y < y:
    if x- ave_x > y-ave_y:
        print(h-y)
    elif x -ave_x < ave_y - y:
        print(w-x)
else:
    if x > ave_x and ave_y ==y:
        print(w-x)
    elif x< ave_x and ave_y == y:
        print(x)
    elif y > ave_y and ave_x == y:
        print(h-y)
    elif y < ave_y and ave_x ==x:
        print(x)
    else:
        print(x)
