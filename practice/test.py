import sys
import os
import parser

dir = os.path.dirname(os.path.realpath(__file__))
# read file
parser.parse_input(os.path.join(dir, "a_an_example.in.txt"))
