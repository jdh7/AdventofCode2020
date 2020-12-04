
#======= AoC Day 3 =======

import sys
import fileinput
import math

df = [line.strip() for line in fileinput.input()]

# Open squares = . 
# Tree squares = #

# The patterns for each row repeat ad infinitum.  Once we get to the edge of
# the provided map, we need to loop back through the next provided row. 

def elf_maps(graph, interval, d_interval=1):
    count = 0
    row = 0
    col = 0

    while row+1 < len(graph):
        col += interval
        row += d_interval
        
        if graph[row][col % 31] == "#":
            count += 1
        else:
            pass
    
    print("There's {} trees".format(count))
    return count


a = elf_maps(df, 1)
b = elf_maps(df, 3)
c = elf_maps(df, 5)
d = elf_maps(df, 7)
e = elf_maps(df, 1, 2)


print(a*b*c*d*e)
