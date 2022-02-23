import sys

# read file
with open("a_an_example.in.txt") as f:
    lines = f.read().splitlines()

# get number of clients C
C = lines[0]

# init likes and dislikes
L, D = [], []

# loop on data
for i in range(1, len(lines), 2):
    L.append(lines[i].split(" ")[1:])
    D.append(lines[i+1].split(" ")[1:])

