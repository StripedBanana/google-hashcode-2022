import sys

sys.path.append(".")

from model.project import Project
from model.contributor import Contributor


def parse_input(path):
    contributors = []
    projects = []

    with open(path) as f:
        lines = f.read().splitlines()

    currentLine = 0
    # Parse contributors
    contributorCount, projectCount = lines[0].split(" ")
    for i in range(0, int(contributorCount)):
        currentLine += 1
        contributorName, skillCount = lines[currentLine].split(" ")
        skills = dict()
        for j in range(0, int(skillCount)):
            currentLine += 1
            skillName, skillLevel = lines[currentLine].split(" ")
            skills[skillName] = skillLevel
        contributors.append(Contributor(contributorName, skills))

    for i in range(0, int(projectCount)):
        currentLine += 1
        projectName, completionTime, reward, bestBefore, roleCount = lines[currentLine].split(" ")
        roles = dict()
        for j in range(0, int(roleCount)):
            currentLine += 1
            roleName, roleSkillCap = lines[currentLine].split(" ")
            roles[roleName] = roleSkillCap
        projects.append(Project(projectName, completionTime, reward, bestBefore, roles))
    
    return contributors, projects

def dump_output(outputpath, projectList):
    with open(outputpath, "w") as f:
        f.write(len(projectList))
        for project in projectList:
            f.write(project.name)
            f.write(project.contributors)
