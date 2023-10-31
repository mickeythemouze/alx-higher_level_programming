#!/usr/bin/python3
for i in range(100):
    print(f"{i:02d}", end="{}".format(", ") if i < 99 else "\n")
