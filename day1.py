#!/usr/bin/env python3

data = open("input1.txt", "r").read().split("\n")

elves = []
s = 0
for line in data:
    if not line:
        elves.append(s)
        s = 0
    else:
        s += int(line)

# Part 1
print(max(elves))

# Part 2
print(sum(sorted(elves)[-3:]))
