import sys
sys.path.append(".")

from model.project import Project
from model.contributor import Contributor

import model.project

Projects = list[Project]
def run(contrib, projects):

    # day 0
    D = 0

    # finished projects
    finished_projects: Projects = []
    while (len(finished_projects) < len(projects)):
        add_project(projects)
        finished_projects = check_projects(projects, finished_projects, D)

        D+=1
    return finished_projects


def update_skill_levels(projects: Projects):
    for project in projects:
        for k, v in project.roles.items():
            if v.contributor.skills[k] >= v.cap:
                v.contributor.skills[k] += 1
        
def check_projects(projects: Projects, finished_projects: Projects, D):
    for project in projects:
        for k, v in project.roles.items():
            if v.contributor != "":
                # if every role is filled, decrement project required time
                project.requiredTime -= 1
        if project.bestBeforeCompletion < (D + project.requiredTime):
            for contributor in project.contributors:
                contributor.busy = False
        if project.requiredTime == 0:
            # if project is done
            finished_projects.append(project)
            update_skill_levels(project)
            for contributor in project.contributors:
                contributor.busy = False


def add_project():
    print("t")
