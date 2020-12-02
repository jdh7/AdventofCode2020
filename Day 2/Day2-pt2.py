# ======= Advent of Code day 2 =======
import sys
import fileinput

# sample imput ['1-3', 'a:', "abcde"]
df = [line.strip().split(" ") for line in fileinput.input()]

# still messily cleaning the input like a noob because this is pt 2. 
x = []
for i in df:
    x.append(list(map(int, (i[0].split("-")))))

y =[]
for i in df:
    y.append(i[1].strip(":"))

X = []
for i in range(len(df)):
    X.append([x[i], y[i], df[i][2]])

# Count all passwords which contain the certain character in the XOR indexes.  

def New_pw_check(pws):
    count = 0
    for pw in pws:
        pos1 = (pw[0][0])-1
        pos2 = (pw[0][1])-1
        if (pw[2][pos1] == pw[1]) ^ (pw[2][pos2] == pw[1]):
            count += 1
        else:
            pass
    print(count)

New_pw_check(X)
