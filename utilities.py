def read_file(path):
    lines = []

    with open(path, "r") as f:
        for line in f:
            lines.append(line.rstrip())

    return lines


def etl(array, func):
    return list(map(func, array))
