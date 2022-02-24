import sys

def parse_input(path):
    contributors = []
    projects = []

    with open(path) as f:
        lines = f.read().splitlines()
    currentLine = 1

    # Parse contributors
    contributorCount, projectCount = line[0].split(" ")
    for i in xrange(0, contributorCount):
        contributorName, skillCount = line[currentLine].split(" ")
        currentLine = currentLine + 1
        skills = []
        for j in xrange(0, skillCount):
            skillName, skillLevel = line[currentLine].split(" ")
            skills.append(Skill(skillName, skillLevel))
        contributors.append(Contributor(contributorName, skills))



    


# get number of clients C
C = lines[0]

# init likes and dislikes
L, D = [], []

# loop on data
for i in range(1, len(lines), 2):
    L.append(lines[i].split(" ")[1:])
    D.append(lines[i+1].split(" ")[1:])
