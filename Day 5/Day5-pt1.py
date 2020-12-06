# ======= AoC Day _ =======

import fileinput
import math
import re

# I have 888 tickets, must be a big plane!

tickets = [line.strip() for line in fileinput.input()]

# Go through the tickets and change the row and column until we find the seat.

seatID = 0

for ticket in tickets:
    r = [0, 127]
    col = [0, 7]
    for c in ticket:
        if c == 'F':
            r[1] = int((r[0]+r[1])/2)
        elif c == 'B':
            r[0] = int((r[0]+r[1])/2)+1
        elif c == "L":
            col[1] = int((col[0]+col[1])/2)
        elif c == 'R':
            col[0] = int((col[0]+col[1])/2)+1

# Find out the current seat ID by multiplying the row by 8 and adding the col. 
    a = (r[0])*8 + col[0]

# If the current seat is the highest seat ID, keep it. 
    if a > seatID:
        seatID = a

print("The highest seat ID is: {}.".format(seatID))


