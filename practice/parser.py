import sys

def parse_input(path):
    contributors = []
    projects = []

    with open(path) as f:
        lines = f.read().splitlines()

    currentLine = 0
    # Parse contributors
    contributorCount, projectCount = lines[0].split(" ")
    for i in xrange(0, contributorCount):
        currentLine = currentLine + 1
        contributorName, skillCount = lines[currentLine].split(" ")
        skills = []
        for j in xrange(0, skillCount):
            currentLine = currentLine + 1
            skillName, skillLevel = lines[currentLine].split(" ")
            skills.append(Skill(skillName, skillLevel))
        contributors.append(Contributor(contributorName, skills))

    for i in xrange(0, projectCount):
        currentLine = currentLine + 1
        projectName, completionTime, reward, bestBefore, roleCount = lines[currentLine].split(" ")
        roles = []
        for j in xrange(0, roleCount):
            currentLine = currentLine + 1
            roleName, roleSkillCap = lines[currentLine].split(" ")
            roles.append(Role(roleName, roleSkillCap))
