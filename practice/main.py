import sys
import os
import parserz
import run

if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(directory, "a_an_example.in.txt")

    contributors, projects = parserz.parse_input(input_path)
    
    res = run.run(contributors, projects)