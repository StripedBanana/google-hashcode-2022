import sys
sys.path.append(".")

from model.project import Project
from model.contributor import Contributor

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
        for k, v in projects.roles.items():
            if v.contributor.skills[k] >= v.cap:
                v.contributor.skills[k] += 1
        

def add_project():
    print("t")

def update_contrib(contrib):
    print("t")