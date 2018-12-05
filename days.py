from itertools import cycle


class Day1:
    def __init__(self, changes):
        self.changes = changes

    def solve_p1(self):
        return sum(self.changes)

    def solve_p2(self):
        current, freqs = 0, set()

        for num in cycle(self.changes):
            if current in freqs:
                return current

            freqs.add(current)

            current += num
