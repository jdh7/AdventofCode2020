#======= AoC Day 3 =======

import sys
import fileinput

df = [line.strip() for line in fileinput.input()]
# print(df[0], len(df))

# Open squares = . 
# Tree squares = #

# The patterns for each row repeat ad infinitum.  Once we get to the edge of
# the provided map, we need to loop back through the next provided row. 

# There's got to be a less smooth brain way to get this pattern.
r = [x for x in range(0, 31, 3)]
t = [x for x in range(2, 31, 3)]
u = [x for x in range(1, 31, 3)]

rtu = r+t+u
print(rtu)

# Right 3, down 1.
def elf_maps(graph):
    count = 0
    for i in range(len(graph)):
        c = rtu[i % 31]
        if graph[i][c] == "#":
            count += 1
        else:
            pass
    print("There's {} trees".format(count))

elf_maps(df)
