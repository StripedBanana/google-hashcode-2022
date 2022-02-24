import sys

sys.path.append(".")

from model.project import Project
from model.contributor import Contributor
from model.role import Role
from model.skill import Skill


def parse_input(path):
    contributors = []
    projects = []

    with open(path) as f:
        lines = f.read().splitlines()

    currentLine = 0
    # Parse contributors
    contributorCount, projectCount = lines[0].split(" ")
    for i in range(0, int(contributorCount)):
        currentLine = currentLine + 1
        contributorName, skillCount = lines[currentLine].split(" ")
        skills = []
        for j in range(0, int(skillCount)):
            currentLine = currentLine + 1
            skillName, skillLevel = lines[currentLine].split(" ")
            skills.append(Skill(skillName, skillLevel))
        contributors.append(Contributor(contributorName, skills))

    for i in range(0, int(projectCount)):
        currentLine = currentLine + 1
        projectName, completionTime, reward, bestBefore, roleCount = lines[currentLine].split(" ")
        roles = []
        for j in range(0, int(roleCount)):
            currentLine = currentLine + 1
            roleName, roleSkillCap = lines[currentLine].split(" ")
            roles.append(Role(roleName, roleSkillCap))
        projects.append(Project(projectName, completionTime, reward, bestBefore, roles))
    
    return contributors, projects

def dump_output(outputpath, projectList):
    with open(outputpath, "w") as f:
        f.write(len(projectList))
        for project in projectList:
            f.write(project.name)
            f.write(project.contributors)
