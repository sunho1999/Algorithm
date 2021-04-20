import sys
num = int(sys.stdin.readline())
s = set()
for i in range(num):
    cmd = sys.stdin.readline().strip().split()

    if len(cmd) == 1:
       if cmd[0] == "all":
           s = set([i for i in range(1,21)])
       else:
           s = set()
       continue

    a = cmd[0]
    b = cmd[1]
    b = int(b)
    if a == "add":
        s.add(b)
    elif a == "remove":
        s.discard(b)
    elif a == "check":
        if b in s:
            print(1)
        else:
            print(0)
    elif a == "toggle":
        if b in s:
            s.discard(b)
        else:
            s.add(b)