"""
 File: wiresL.py
 Course: COMPSCI 320

 Name: John David Brawn
 UPI: jbra988
 ID: 881548616
 Email: jdbrawn@bu.edu
"""

import sys

with open('wiresL.txt') as f:
    lines = f.readlines()
#lines = sys.stdin.readlines()

counter = 1
for i in range(int(lines[0])):
    n = int(lines[counter])
    counter += 1

    length = []

    for j in range(counter, counter+n):
        a, b = lines[j].split()
        length.append(abs(int(a)-int(b)))

    maxLength = int(max(length))

    finalString = ""
    for j in range(n):
        if length[j] == maxLength:
            finalString += " " + str(j+1)

    print("Case #" + str(i+1) + ":" + finalString)

    counter += n