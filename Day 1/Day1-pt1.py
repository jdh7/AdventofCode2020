# ======== AoC Day 1 =======
# QUICK SOLVE
#
#
# with open("data.txt") as f:
#     content = f.readlines()
# content = [int(x.strip()) for x in content]

# def ExpenseReport(expenses):
#     for i in expenses:
#         for j in range(len(expenses)):
#             if i + expenses[j] == 2020:
#                 print("The i is {}, j is {}, and the product is {}".format(i, expenses[j], i*expenses[j]))
#                 return

# ExpenseReport(content)
#
#
# CLEANED UP A BIT. 

import sys
import fileinput

rpt = [int(line) for line in fileinput.input()]

def ExpRep(expenses):
    for i in range(len(expenses)):
        for j in range(i+1, len(expenses)):
            if expenses[i]+expenses[j] == 2020:
                print("The product is {}".format(expenses[i]*expenses[j]))
                return

ExpRep(rpt)

