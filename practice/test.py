import sys
import os
import parser

dir = os.path.dirname(os.path.realpath(__file__))
# read file
contributors, projects = parser.parse_input(os.path.join(dir, "a_an_example.in.txt"))

for contributor in contributors:
    print(contributor.__dict__)

for project in projects:
    print(project.__dict__)

