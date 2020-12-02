
# # ======== AoC Day 1 =======
# 
# INITIAL QUICK SOLVE:
#
#
# with open("data.txt") as f:
#     content = f.readlines()
# content = [int(x.strip()) for x in content]

# def ExpenseReport(expenses):
#     for i in expenses:
#         for j in range(len(expenses)):
#             for k in range(len(expenses)):
#                 if (i + expenses[j] + expenses[k]) == 2020:
#                     print("The i is {}, j is {}, k is {} and the product is {}".format(i, expenses[j], expenses[k], i*expenses[j]*expenses[k]))
#                     return

# ExpenseReport(content)

# CLEANED UP A BIT. 

import sys
import fileinput

rpt = [int(line) for line in fileinput.input()]

def ExpRep(expenses):
    for i in range(len(expenses)):
        for j in range(i+1, len(expenses)):
            for k in range(j+1, len(expenses)):
                if expenses[i]+expenses[j] + expenses[k] == 2020:
                    print("The product is {}".format(expenses[i]*expenses[j]*expenses[k]))
                    return

ExpRep(rpt)

