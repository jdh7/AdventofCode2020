# ======= AoC Day 6 =======

import fileinput
import math
import re

group = {}
members = 0
total = 0
valid = 0 

# Implement terrible search for how many questions all members of a boarding
# group answered yes to. 

for line in fileinput.input():
    line = line.strip()
    if not line:
        for i in group:
            if group[i] == members:
                valid += 1
        total += valid 
        group = {}
        members = 0
        valid = 0
    else:
        for i in line:
            group[i] = group.get(i, 0) + 1 
        members += 1
            
print("The sum of groups is {}".format(total))


