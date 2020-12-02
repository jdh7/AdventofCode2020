# ======= Advent of Code day 2 =======
import sys
import fileinput

# sample imput ['1-3', 'a:', "abcde"]
df = [line.strip().split(" ") for line in fileinput.input()]

# cleaning up the input like a noob 
x = []
for i in df:
    x.append(list(map(int, (i[0].split("-")))))

y =[]
for i in df:
    y.append(i[1].strip(":"))

X = []
for i in range(len(df)):
    X.append([x[i], y[i], df[i][2]])

# Count all passwords which contain the correct amount of certain character.

def pw_check(pws):
    count = 0
    for pw in pws:
        if (pw[2].count(pw[1]) >= pw[0][0]) and (pw[2].count(pw[1]) <= pw[0][1]):
          count += 1
        else:
            pass
    print(count)

pw_check(X)

