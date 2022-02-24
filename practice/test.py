import sys
import os
import parserz

dir = os.path.dirname(os.path.realpath(__file__))
# read file
contributors, projects = parserz.parse_input(os.path.join(dir, "a_an_example.in.txt"))

print(">> Contributors")
for contributor in contributors:
    print(contributor.__dict__)

print(">> Projects")
for project in projects:
    print(project.__dict__)

