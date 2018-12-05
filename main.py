#!/Users/antoine/dev/personal/AoC/venv/bin/python

from itertools import cycle

from days import Day1
from utilities import *

##################################
#             DAY 1              #
##################################
lines = read_file("resources/day1-input.txt")
changes = etl(lines, int)
day = Day1(changes)

# Part 1
print(day.solve_p1())

# Part 2
print(day.solve_p2())
