#!/Users/antoine/dev/personal/AoC/venv/bin/python

from itertools import cycle

from utilities import *

##################################
#             DAY 1              #
##################################

lines = read_file("resources/day1-input.txt")
changes = etl(lines, int)

# Part 1
print(sum(changes))

# Part 2
current, freqs = 0, set()

for num in cycle(changes):
    if current in freqs:
        break

    freqs.add(current)

    current += num

print(current)
