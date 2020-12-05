# ======= AoC day 4 =======
import fileinput
elf = {}
passports = []

# Add all the identifications to a passport dictionary
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

# Sort through the passports to find the initially valid
passports2 = []
for i in passports:
    if len(i) == 8 or (len(i) == 7 and ('cid' not in i)):
        passports2.append(i)
    else:
        pass

# 'Normalize' the height data
for i in passports2:
    if i['hgt'][-2:] == "cm":
        i['hgt'] = int(i['hgt'].strip('cm'))
    elif i['hgt'][-2:] == "in":
        i['hgt'] = int(i['hgt'].strip('in')) + 1000
    else:
        i['hgt'] = 0

# 'Normalize' the hair color data by creating a list of acceptable hair color
# characters and checking each elf's hair color
chars = {'#', 'a','b','c','d','e','f'}
for i in range(10):
    chars.add(str(i))

for i in passports2:
    if len(i['hcl']) != 7:
        i['hcl'] = 0
    elif i['hcl'][0] != '#':
        print("hcl: {}".format(i['hcl']))
        i['hcl'] = 0
    else:
        for j in i['hcl']:
            if j not in chars:
                i['hcl'] = 0
            else:
                pass

# Check each elf's ID and count the valid.
def elf_checker_2(ppts):
    eyes = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    valid = 0
    for i in ppts:
        a = (int(i["byr"]) > 1919 and int(i["byr"]) < 2003)
        b = (int(i["iyr"]) > 2009 and int(i["iyr"]) < 2021)
        c = (int(i["eyr"]) > 2019 and int(i["eyr"]) < 2031)
        d = ((i["hgt"] > 149 and i["hgt"] < 194) or (i["hgt"] < 1077 and i["hgt"] > 1058))
        e = (str(i["ecl"]) in eyes) 
        f = (len(i["pid"]) == 9) 
        g = (i["hcl"] != 0)
        
        if a and b and c and d and e and f and g:
            valid += 1
        else:
            pass
    print("There are {} valid passports.".format(valid))

elf_checker_2(passports2)
