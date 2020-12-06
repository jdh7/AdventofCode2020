# ======= AoC Day 6 =======

import fileinput
import math
import re

group = []  
total = 0

for line in fileinput.input():
    line = line.strip()
    if not line:
        total += (len(group))
        group = []
    else:
        for i in line:
            if i not in group:
                group.append(i)

print("The sum of groups is {}".format(total))
# print("Len(grp):{}".format(len(group)))

