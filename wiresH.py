"""
 File: wiresH.py
 Course: COMPSCI 320

 Name: John David Brawn
 UPI: jbra988
 ID: 881548616
 Email: jdbrawn@bu.edu
"""

import sys

#with open('wiresL.txt') as f:
#    lines = f.readlines()
lines = sys.stdin.readlines()

def sortAndCount(l):
    lengthL = len(l)
    if lengthL == 1:
        return 0, l

    m = int(lengthL / 2)
    la = l[:m]
    lb = l[m:]

    ra, la = sortAndCount(la)
    rb, lb = sortAndCount(lb)
    rab, lp = mergeAndCount(la, lb)

    return ra+rb+rab, lp

def mergeAndCount(la, lb):
    i = 0
    j = 0
    rab = 0
    lp = []
    while i < len(la) and j < len(lb):
        if la[i] < lb[j]:
            lp.append(la[i])
            i += 1
        else:
            lp.append(lb[j])
            rab += (len(la) - i)
            j += 1

    lp.extend(la[i:])
    lp.extend(lb[j:])
    return rab, lp

counter = 1
for i in range(int(lines[0])):
    n = int(lines[counter])
    counter += 1

    original = []
    for j in range(counter, counter+n):
        a, b = lines[j].split()
        original.append([int(a), int(b)])

    original.sort()
    bees = [k[1] for k in original]

    print("Case #" + str(i+1) + ": " + str(sortAndCount(bees)[0]))
    counter += n