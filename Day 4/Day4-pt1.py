# ======= AoC day 4 =======

# A passport is valid if:
#   -has 8 fields reported.
#   -has 7 fields reported, excluding CID.

import fileinput
# Input the elf passport data into a dictionary.
elf = {}
passports = []
cid = 'cid'

for line in fileinput.input():
    line = line.strip()
    if not line:
        passports.append(elf)
        elf = {}
    else:
        words = line.split()
        for word in words:
            k, v = word.split(':')
            elf[k] = v

# Iterate through the passports, count if valid.

def Passport_check(ppts):
    passes = 0
    for i in ppts:
        if len(i) == 8 or (len(i) == 7 and (cid not in i)):
            passes += 1
        else:
            pass
    print("There are {} passes.".format(passes))

Passport_check(passports)
