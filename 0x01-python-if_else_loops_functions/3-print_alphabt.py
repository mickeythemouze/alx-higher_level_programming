#!/usr/bin/python3
for lower in range(ord('a'), ord('z') + 1):
    excep = chr(lower)
    if excep != 'q' and excep != 'e':
        print(excep, end="{}".format(""))
