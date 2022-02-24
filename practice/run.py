import sys
sys.path.append(".")

from model.project import Project
from model.contributor import Contributor
from model.role import Role
from model.skill import Skill

import model.project

def run(contrib, projects):

    # day 0
    D = 0
    while(True):

        update_skill_levels(projects)

        add_project(projects)

        update_contrib(contrib)



        D+=1

Projects = list[Project]
def update_skill_levels(projects: Projects):
    
    for project in projects:
        for role in projects.roles:
            if role.contributor.skills[role.name] >= role.cap:
                role.contributor.skills[role.name] += 1
        

def add_project():
    print("t")

def update_contrib(contrib):
    print("t")