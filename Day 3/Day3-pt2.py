
#======= AoC Day 3 =======

import sys
import fileinput
import math

df = [line.strip() for line in fileinput.input()]

# Open squares = . 
# Tree squares = #

# The patterns for each row repeat ad infinitum.  Once we get to the edge of
# the provided map, we need to loop back through the next provided row. 

# Crudely create a list of all the indexes that appear for each interval size

def listmaker(size):
    r = [i for i in range(0,31,size)]
    a = size
    for t in range(size-1):
        a -= 1
        r += [i for i in range(a,31,size)]
    print("lenght of r: {}, and r: {}".format(len(r), r))
    return r

# Count the trees appearing at the correct [interval x d_interval]

def elf_maps(graph, interval, d_interval=1):
    count = 0
    rtu = listmaker(interval)
    l = math.ceil((len(graph))/d_interval)
    print("the len of graph is {}, the l is:{}".format(len(graph), l))

    for i in range(l):
        c = rtu[i % 31]
        i = i*d_interval
        print("the graph[{}][{}] if {}".format(i,c,graph[i][c]))
        if graph[i][c] == "#":
            count += 1
        else:
            pass
    print("There's {} trees".format(count))
    return count

def elfchecker(graph):
    count = 0
    for i in range(len(graph)):
        c = i % 31
        # print("a1 i: {}, c:{}".format(i, c))
        if graph[i][c] == "#":
            count += 1
        else:
            pass
    print("There's fhfhfhfh {} trees".format(count))



a = elf_maps(df, 1, 1)
# b = elf_maps(df, 3, 1)
# c = elf_maps(df, 5, 1)
# d = elf_maps(df, 7, 1)
# e = elf_maps(df, 1, 2)
a1 = elfchecker(df)

print(a, a1)
