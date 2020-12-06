# ======= AoC Day _ =======

import fileinput
import math
import re

# I have 888 tickets, must be a big plane!

tickets = [line.strip() for line in fileinput.input()]

# Go through the tickets and change the row and column until we find the seat.

seatID = 0
seats = []
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

# Create a list of all the seat ID's
    a = (r[0])*8 + col[0]
    seats.append(a)

# Sort the seats
seats = sorted(seats) 

# Go through the seats and return the missing seat. 
def wheres_my_seat(taken):
    y = 6
    for i in taken:
        if i == y:
            y+=1
        elif i != y:
            print("My seat is {}.".format(i-1))
            return

wheres_my_seat(seats)
